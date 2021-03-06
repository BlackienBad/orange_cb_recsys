from unittest import TestCase

from orange_cb_recsys.content_analyzer.field_content_production_techniques.tf_idf import LuceneTfIdf
from orange_cb_recsys.content_analyzer.information_processor.nlp import NLTK
from orange_cb_recsys.content_analyzer.raw_information_source import JSONFile


class TestLuceneTfIdf(TestCase):
    def test_produce_content(self):
        file_path = '../../../datasets/movies_info_reduced.json'
        try:
            with open(file_path):
                pass
        except FileNotFoundError:
            file_path = 'datasets/movies_info_reduced.json'

        technique = LuceneTfIdf()
        technique.set_field_need_refactor("Plot")
        technique.set_pipeline_need_refactor(str(1))
        technique.set_processor_list([NLTK()])
        technique.dataset_refactor(JSONFile(file_path), ["imdbID"])
        features_bag_test = technique.produce_content("test", "tt0113497", "Plot")
        features = features_bag_test.get_value()

        self.assertEqual(features['years'], 0.6989700043360189)

