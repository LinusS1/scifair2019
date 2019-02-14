"""Tests for the analyzers to make sure nothing breaks/stops working when I update them"""
from unittest import TestCase
import unittest
from .misspelled_words_analyzer import MisspellingsAnalyzer
from .length_of_words_analyzer import LengthOfWordsAnalyzer
from .negitive_words import NegativeScore
from .type_of_words_analyzer import WordTypesAnalyzer
from .word_case_analyzer import CapsScore


class TestMisspellingsAnalyzer(TestCase):
    """Test the misspellings analyzer"""

    def test_process_misspellings(self):
        """Test that misspelling are counted"""
        analyzer = MisspellingsAnalyzer("Buiild the wall, noow!", "politician")
        self.assertEqual(analyzer.process(), (0.5, "politician"))

    def test_process_misspellings_case(self):
        """Test that text with weird case is okay"""
        analyzer = MisspellingsAnalyzer("BIG NEWS: WALLL IS BUILTT!", "news")
        self.assertEqual(analyzer.process(), (0.2, "news"))

    def test_process_no_misspellings(self):
        """Test text with no misspellings"""
        analyzer = MisspellingsAnalyzer("Spelling is needed for high school.", "news")
        self.assertEqual(analyzer.process(), (0, "news"))


class TestLengthOfWordsAnalyzer(TestCase):
    """Test the length of words analyzer"""

    def test_process_length(self):
        analyzer = LengthOfWordsAnalyzer("very huge gene", "scientist")
        self.assertEqual(analyzer.process(), (4.0, "scientist"))


class TestNegativeScore(TestCase):
    def test_process_no_negitive_words(self):
        analyzer = NegativeScore("We've found a wounderful new type of worm!", "scientist")
        self.assertEqual(analyzer.process(), (0, "scientist"))

    def test_process_some_negative_words(self):
        analyzer = NegativeScore("I've heard some depressing stories.", "scientist")
        self.assertEqual(analyzer.process(), (0.2, "scientist"))

    def test_process_all_negative_words(self):
        analyzer = NegativeScore("Lame, abandoned", "news")
        self.assertEqual(analyzer.process(), (1, "news"))


class TestWordTypesAnalyzer(TestCase):
    def test_process(self):
        analyzer = WordTypesAnalyzer("I am running for president", "politician")
        self.assertEqual(analyzer.process(), ([('I', 'PRP'), ('am', 'VBP'), ('running', 'VBG'), ('for', 'IN'),
                                               ('president', 'NN')], "politician"))


class TestCapsScore(TestCase):
    def test_process_no_caps(self):
        analyzer = CapsScore("hello there!", "someone")
        self.assertEqual(analyzer.process(), (0, "someone"))

    def test_process_some_caps(self):
        analyzer = CapsScore("ATTENTION: schools", "politician")
        self.assertEqual(analyzer.process(), (0.5625, "politician"))

    def test_process_all_caps(self):
        analyzer = CapsScore("BREAKING NEWS", "news")
        self.assertEqual(analyzer.process(), (1, "news"))

