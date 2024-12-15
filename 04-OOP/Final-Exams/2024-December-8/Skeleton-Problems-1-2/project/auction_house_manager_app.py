from typing import List

from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact

from project.collectors.base_collector import BaseCollector
from project.collectors.private_collector import PrivateCollector
from project.collectors.museum import Museum


class AuctionHouseManagerApp:

    ARTIFACTS_TYPES = {"RenaissanceArtifact": RenaissanceArtifact,
                       "ContemporaryArtifact": ContemporaryArtifact}
    COLLECTORS_TYPES = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: List[BaseArtifact] = []
        self.collectors: List[BaseCollector] = []

    def find_collector_by_name(self, name_of_collector: str):
        return next((c for c in self.collectors if c.name == name_of_collector), None)

    def find_artifact_by_name(self, name_of_artifact: str):
        return next((a for a in self.artifacts if a.name == name_of_artifact), None)

    def register_artifact(self, artifact_type: str, artifact_name: str,
                          artifact_price: float, artifact_space: int):
        if artifact_type not in self.ARTIFACTS_TYPES:
            raise ValueError("Unknown artifact type!")

        if self.find_artifact_by_name(artifact_name):
            raise ValueError(f"{artifact_name} has been already registered!")

        new_artifact = self.ARTIFACTS_TYPES[artifact_type](artifact_name,
                                                           artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.COLLECTORS_TYPES:
            raise ValueError("Unknown collector type!")

        if self.find_collector_by_name(collector_name):
            raise ValueError(f"{collector_name} has been already registered!")

        new_collector = self.COLLECTORS_TYPES[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self.find_collector_by_name(collector_name)
        artifact = self.find_artifact_by_name(artifact_name)

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the "
                             f"auction!")

        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the "
                             f"auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of " \
               f"{artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = self.find_artifact_by_name(artifact_name)

        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        selected_collectors = [c.increase_money() for c in self.collectors if
                               c.available_money <= max_money]

        return f"{len(selected_collectors)} collector/s increased their available money."

    def get_auction_report(self):
        sorted_collectors = sorted(self.collectors,
                                   key=lambda x: (-len(x.purchased_artifacts), x.name))
        sold_artifacts = [len(c.purchased_artifacts) for c in self.collectors]
        info_collectors = '\n'.join([str(c) for c in sorted_collectors])

        return f"**Auction statistics**\n" \
               f"Total number of sold artifacts: {sum(sold_artifacts)}\n" \
               f"Available artifacts for sale: {len(self.artifacts)}\n***\n" \
               f"{info_collectors}"
