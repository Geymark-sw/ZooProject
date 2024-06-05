import unittest
from unittest import TestCase
from src.Zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def test_animal_dimension(self):

        """
            Questa funzione controlla che gli animali troppo grandi non vengano inseriti
        """

        zookeeper_1: ZooKeeper = ZooKeeper("Gianni","Rossi",1)
        fence_1: Fence = Fence(100, 25.0, "Savana")
        animal_1: Animal("Pluto", "Canide", 5, 300.0, 1.0, "Savana")
        result: int = len(fence_1.animals)
        message: str = f"Erroer: the function add_animall should not add self.animal_1 into self.fence_1"

        self.assertEqual(result, 0, message)
