# pylint: disable=unused-argument

from dagster import DependencyDefinition, InputDefinition, PipelineDefinition, pipeline, solid


@solid
def return_one(context):
    return 1


@solid(input_defs=[InputDefinition("number", int)])
def add_one(context, number):
    return number + 1


@pipeline
def one_plus_one_pipeline():
    add_one(return_one())


one_plus_one_pipeline_def = PipelineDefinition(
    name='one_plus_one_pipeline',
    solid_defs=[return_one, add_one],
    dependencies={'add_one': {'number': DependencyDefinition('return_one')}},
)
