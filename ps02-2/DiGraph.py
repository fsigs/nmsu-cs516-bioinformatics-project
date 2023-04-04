
from pyllist import dllist
from random import choice

class Node:

  def __init__(self, label: str):
    self.label = label
    self.incoming = 0
    self.outgoing = dllist()

class DiGraph:

  def __init__(self):
    self.nodes = []

  def get_sink(self):
    None
  
  def get_source(self):
    None
  
  def has_eulerian_cycle(self):
    None
  
  def get_eulerian_cycle(self):
    None
  
  def get_eulerian_path(self):
    None
  
  def DNA_hasher(self, seq):
    None

  def build_sequence(self, path: dllist):
    None
