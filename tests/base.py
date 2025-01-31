"""
Declares parent class for test classes.
"""

# Third Party
import logging
import os
import unittest


class TestCaseBase(unittest.TestCase):
    """
    Parent class for all specific test classes.
    """

    fixtures_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures")

    def __init__(self, *args, **kwargs):
        # configure logging
        logger = logging.getLogger(__name__)

        # initialize parent class
        super().__init__(*args, **kwargs)

    def _compare_seqs(self, obj_seq1, obj_seq2, properties):
        """Given two sequences, ensure that they are the same length, and that each specified
        property is equal per object. This method explodes if the sequences are not the same
        as defined by assertEqual on the properties of interest.

        Args:
            obj_seq1: list | tuple
                List or tuple sequence.
            obj_seq2: list | tuple
                List or tuple sequence.
            properties: list(str) | tuple(str)
                attributes whose values will be compared across sequences.
        """
        self.assertEqual(len(obj_seq1), len(obj_seq2))
        for obj1, obj2 in zip(obj_seq1, obj_seq2):
            for prop in properties:
                self.assertEqual(getattr(obj1, prop), getattr(obj2, prop))
