#!/usr/bin/python3

import argparse
import pathlib

from pyvis.network import Network

GTAGS_VAR_PREFIX = "__."
GTAGS_VAR_NEXTKEY = "__.NEXTKEY"

network_options = """
var options = {
  "nodes": {
    "borderWidthSelected": 3,
    "color": {
      "highlight": {
        "border": "rgba(233,178,185,1)",
        "background": "rgba(255,0,4,1)"
      },
      "hover": {
        "border": "rgba(174,233,158,1)",
        "background": "rgba(27,255,0,1)"
      }
    },
    "font": {
      "strokeWidth": 3
    },
    "scaling": {
      "min": 0,
      "max": 27
    },
    "shapeProperties": {
      "borderRadius": 5
    },
    "size": 10
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.45
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": {
      "type": "cubicBezier",
      "forceDirection": "none",
      "roundness": 0.3
    }
  },
  "interaction": {
    "hover": true,
    "keyboard": {
      "enabled": true
    },
    "multiselect": true,
    "navigationButtons": true
  },
  "physics": {
    "hierarchicalRepulsion": {
      "centralGravity": 0.35,
      "springLength": 200,
      "nodeDistance": 165,
      "damping": 0.05
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }
}
"""


def generate_graph(nodes, edges):
  g = Network(height=None, width=None)
  g.add_nodes(list(nodes.keys()), label=list(nodes.values()))
  g.add_edges(edges)
  g.set_options(network_options)
  g.show("network.html")


def parse_tags(tag, rtag, path):
  sym = {}
  nodes = {}
  edges = []

  with path.open() as pf:
    for p_line in pf:
      p = p_line.strip().split("\t")
      if p[0][:len(GTAGS_VAR_PREFIX)] == GTAGS_VAR_PREFIX:
        # Skip meta data line for tags
        continue

      if len(p) > 2 and p[2] == 'o':
        # These are file entry that does not have any symbols, just ignore these
        continue

      # Actually process the line entry.

      # There is two possible entry format from the gtag path file
      # One is to map file name to index, the other index to file name.
      # We should use one to create new node entry, and other to verify entry, or mostly just ignore it
      if not p[0].isdigit() and p[1].isdigit():
        nodes[int(p[1])] = p[0]
      elif p[0].isdigit() and not p[1].isdigit():
        assert nodes[int(p[0])] == p[1]

  with tag.open() as tf:
    for t_line in tf:
      t = t_line.strip().split("\t")
      if t[0][:len(GTAGS_VAR_PREFIX)] == GTAGS_VAR_PREFIX:
        # Skip meta data line for tags
        continue

      node_idx = int(t[1].split()[0])
      assert node_idx in nodes
      sym[t[0]] = node_idx

  with rtag.open() as rf:
    for r_line in rf:
      r = r_line.strip().split("\t")
      if r[0][:len(GTAGS_VAR_PREFIX)] == GTAGS_VAR_PREFIX:
        # Skip meta data line for tags
        continue

      ref_node_idx = int(r[1].split()[0])
      edge_weight = len(r[1].split()[2].split(","))
      if r[0] in sym and ref_node_idx != sym[r[0]]:
        edges.append((ref_node_idx, sym[r[0]], edge_weight*0.05))

  return nodes, edges


def parse_args():
  parser = argparse.ArgumentParser(description='Process tag files.')
  parser.add_argument('-t', '--tag-file', dest='tag_file', help='Symbol tag file', required=True)
  parser.add_argument('-r',
                      '--r-tag-file',
                      dest='rtag_file',
                      help='Reference tag file',
                      required=True)
  parser.add_argument('-p',
                      '--path-tag-file',
                      dest='path_file',
                      help='Path tag file',
                      required=True)

  return parser.parse_args()


def main():
  args = parse_args()
  nodes, edges = parse_tags(pathlib.Path(args.tag_file), pathlib.Path(args.rtag_file),
                            pathlib.Path(args.path_file))
  generate_graph(nodes, edges)


if __name__ == "__main__":
  main()
