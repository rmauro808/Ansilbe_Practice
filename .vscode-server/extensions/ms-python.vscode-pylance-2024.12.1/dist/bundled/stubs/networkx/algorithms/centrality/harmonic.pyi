from functools import partial
from typing import Mapping

from ...classes.graph import Graph

__all__ = ["harmonic_centrality"]

def harmonic_centrality(G: Graph, nbunch=None, distance=None, sources=None) -> Mapping: ...
