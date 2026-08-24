# Connector Write and Patch Application Strategy

**Context class:** `conditional-deep-reference`

Load when a GitHub connector operation will write file/blob content or when a patch must be transported/applied remotely.

## Observed connector write ceiling

Historical agent turns have shown a consistent empirical connector write limit of approximately 20 KB per individual content write. Writes above that boundary may be silently truncated without the connector returning an error. This is an observed connector behavior, not a documented GitHub API limit.

Use **19 KB of UTF-8 content as the hard per-write safety ceiling**.

The ceiling applies to each individual content-bearing connector operation, including `create_file`, `update_file`, and each `create_blob` call. An atomic Git tree/commit does not remove the per-blob write ceiling.

Before repository mutation:

1. compute or estimate the UTF-8 byte size of every individual content write;
2. choose the least-complex safe strategy below;
3. record the intended base commit and changed-path set;
4. fail closed if content size, checksum, base identity, or intended scope cannot be verified.

## Strategy selection

### 1. Direct write

Use when every individual content write is `<=19 KB` UTF-8.

Preferred forms:

- one small file: `create_file` or compare-and-swap `update_file`;
- coherent multi-file change: one `create_blob` per file, then `create_tree` → `create_commit` → non-forced `update_ref`.

Requirements:

- size-check each content write independently;
- re-fetch or compare resulting blob/content when correctness matters;
- verify the resulting changed-path set;
- do not split one logical text file into multiple repository files merely to evade the limit.

### 2. Single compressed patch payload

Use when direct file/blob writes are unsuitable and a unified patch is the appropriate transport.

1. Produce the exact unified patch against the recorded base commit.
2. Compute SHA-256 of the original patch bytes.
3. Compress deterministically with gzip (`mtime=0` or equivalent).
4. Base64-encode the compressed bytes as a single ASCII stream with **no line wrapping or trailing newline**.
5. Compute SHA-256 of the exact encoded stream.
6. If the encoded payload is `<=19 KB`, persist it as one connector content write.
7. Persist small metadata separately: original patch checksum, encoded checksum, base commit, and exact intended changed paths.
8. In the application environment:
   - verify encoded checksum before decoding;
   - Base64-decode and decompress;
   - verify original patch checksum;
   - verify current source/base authority;
   - run `git apply --check`;
   - apply transactionally;
   - run `git diff --check`;
   - verify the changed-path set exactly matches intended scope;
   - verify expected output blobs when an expected-blob manifest exists;
   - commit only after every check passes.

### 3. Fragmented compressed patch payload

Use when the compressed Base64 stream exceeds 19 KB.

1. Follow steps 1–5 of the single-payload strategy.
2. Split the **encoded ASCII stream** into deterministic ordered fragments, each `<=19 KB`.
3. Do not insert any byte between fragments:
   - no trailing newline;
   - no whitespace;
   - no delimiter;
   - no JSON/text wrapper;
   - no repeated header.
4. Use zero-padded ordinal names so lexical order equals numeric order.
5. Persist each fragment as one connector content write.
6. Persist the original-patch checksum, encoded-stream checksum, base commit, fragment count, and intended changed-path manifest.
7. Reassemble fragments byte-for-byte in ordinal order.
8. Verify the reconstructed encoded-stream checksum before Base64 decoding.
9. Decode/decompress and verify the original patch checksum.
10. Run `git apply --check`, apply, `git diff --check`, exact changed-path verification, and expected-blob verification before commit.

Any checksum mismatch is a hard failure. Never attempt repair by trimming whitespace, adding padding, reordering fragments heuristically, or regenerating content inside the application workflow.

## Required patch metadata

A remote patch payload should carry or reference:

- `base_commit`;
- `patch_sha256`;
- `encoded_sha256`;
- `encoding`: `gzip+base64`;
- fragment count and deterministic prefix;
- exact intended changed paths;
- expected final blob IDs when practical.

The patch itself remains temporary transport. Ordinary committed source files become authoritative after verified application.

## Workflow/application safety

- Do not include `.github/workflows/**` in a patch applied by a workflow. Update workflow files externally through the connector.
- Verify the branch/source authority immediately before application.
- Check whether expected final blobs already match before applying; if all match, classify as already applied/no-op.
- A failed `git apply` does not prove the change is absent.
- Do not use `--3way`, reject files, fuzzy manual repair, or partial application as a substitute for regenerating a patch against the correct base.
- Run `git diff --check` after application and before commit.
- Compare the exact changed-path set with the intended manifest. Extra or missing paths are a hard failure.
- Clean up temporary payload/fragments only after source authority and required evidence have been verified.

## Tooling

Use `scripts/split_patch.py` to create deterministic gzip+Base64 payload fragments and checksum metadata. Use `templates/github-actions/apply-unified-patch.yml` as the application baseline.

The script defaults to 19,000 encoded bytes per fragment, intentionally below the observed ~20 KB connector boundary.
