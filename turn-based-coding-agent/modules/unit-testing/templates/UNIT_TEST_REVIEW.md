# Unit Test Review

## Target

- Test file/suite:
- Production unit:
- Contract source:

## Findings

| Test / scenario | Classification | Evidence | Smallest correction | Verification |
|---|---|---|---|---|
| | | | | |

Classifications:

- valid test
- missing scenario coverage
- brittle implementation coupling
- invalid fixture
- incorrect expectation
- wrong test level
- isolation/flakiness defect
- weak oracle/assertion
- over-mocking
- coverage gap without proven behavior gap

## Quality checks

- [ ] Scenario and expected outcome are clear from the name.
- [ ] Fixture actually creates the stated preconditions.
- [ ] Expected result is derived independently of current implementation.
- [ ] One coherent behavior is exercised.
- [ ] Assertions are narrow, semantic, and actionable.
- [ ] Test values expose default/ignored/swapped-input defects where relevant.
- [ ] No accidental infrastructure, order, time, random, or global-state dependence.
- [ ] Mocks verify only contractually meaningful interactions.
- [ ] Behavior-preserving refactors should not require assertion changes.
- [ ] Coverage claims are not being used as a substitute for behavior evidence.

## Counterfactual test

Plausible broken implementations that should be caught:

1.
2.
3.

Any that would still pass:

- 

## Recommendation

- Keep / revise / split / move to integration / replace fixture / add coverage:
- Reason:
- Next verification command:
