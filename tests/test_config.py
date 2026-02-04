from confluent_kafka.admin import ConfigResource, ResourceType

from pytest_kafka_broker import KafkaBrokerContext


def test_kafka_broker_extra_config(kafka_broker: KafkaBrokerContext):
    with kafka_broker.admin() as admin:
        (future,) = admin.describe_configs(
            [ConfigResource(ResourceType.BROKER, name="1")]
        ).values()
        assert future.result()["message.max.bytes"].value == "123456"
