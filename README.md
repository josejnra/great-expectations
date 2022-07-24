# Great Expectations

### Concepts

#### Context
A Data Context is the primary entry point for a Great Expectations deployment, with configurations and methods for all supporting components.

#### Datasource
A Datasource provides a standard API for accessing and interacting with data from a wide variety of source systems.

#### Batch Request
A Batch Request is provided to a Datasource in order to create a Batch.

#### Checkpoint
A Checkpoint is the primary means for validating data in a production deployment of Great Expectations.
A Checkpoint runs an Expectation Suite against a Batch (or Batch Request). Running a Checkpoint produces Validation Results. Checkpoints can also be configured to perform additional Actions.

### Commands

```shell
# create new datasource
great_expectations datasource new
# create new expectations suite
great_expectations suite new
# update an existing expectation suite
great_expectations suite edit titanic_expectation_suite
# create a checkpoint
great_expectations checkpoint new titanic_checkpoint
# run a checkpoint
great_expectations checkpoint run titanic_checkpoint
# build docs
great_expectations docs build
```

## Referencies
