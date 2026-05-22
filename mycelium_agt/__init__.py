"""
mycelium-agt — Mycelium Trails community plugin for the AGT EvidenceAnchor SPI.

Implements EvidenceAnchor backed by Mycelium Trails on Arbitrum.
Evidence hashes are written as immutable trail records via the public
argentum.rgiskard.xyz API.

Usage:
    from mycelium_agt import MyceliumAnchor
    anchor = MyceliumAnchor(agent_id="my-agent")
    receipt = anchor.anchor(evidence_hash, metadata={})
    result  = anchor.verify(evidence_hash, receipt)
"""

from .anchor import MyceliumAnchor
from .action_ref import compute_action_ref, format_timestamp
from .types import (
    AnchorReceipt,
    AnchorVerifyResult,
    AnchorVerifyStatus,
    EvidenceAnchor,
    InclusionProof,
)

__version__ = "0.1.1"

__all__ = [
    "MyceliumAnchor",
    "compute_action_ref",
    "format_timestamp",
    "EvidenceAnchor",
    "AnchorReceipt",
    "AnchorVerifyResult",
    "AnchorVerifyStatus",
    "InclusionProof",
    "__version__",
]
