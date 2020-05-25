from unittest import TestCase

from orange_cb_recsys.content_analyzer.field_content_production_techniques.tf_idf import LuceneTfIdf
from orange_cb_recsys.content_analyzer.information_processor.nlp import NLTK
from orange_cb_recsys.content_analyzer.raw_information_source import JSONFile


class TestLuceneTfIdf(TestCase):
    def test_produce_content(self):
        import lucene
        lucene.initVM(vmargs=['-Djava.awt.headless=true'])

        file_path = '../../../datasets/movies_info_test.json'
        try:
            with open(file_path):
                pass
        except FileNotFoundError:
            file_path = 'datasets/movies_info_test.json'

        technique = LuceneTfIdf()
        technique.append_field_need_refactor("Plot", str(1), [NLTK()])
        technique.dataset_refactor(JSONFile(file_path), ["imdbID"])
        features_bag_test = technique.produce_content("test", "tt0113497", "Plot", str(1))
        features = features_bag_test.get_feature_dict()

        self.assertEqual(features['years'], 0)

