# Copyright (c) Alibaba, Inc. and its affiliates.
from typing import TYPE_CHECKING

from modelscope.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .automatic_post_editing_pipeline import AutomaticPostEditingPipeline
    from .conversational_text_to_sql_pipeline import ConversationalTextToSqlPipeline
    from .table_question_answering_pipeline import TableQuestionAnsweringPipeline
    from .dialog_intent_prediction_pipeline import DialogIntentPredictionPipeline
    from .dialog_modeling_pipeline import DialogModelingPipeline
    from .dialog_state_tracking_pipeline import DialogStateTrackingPipeline
    from .document_segmentation_pipeline import DocumentSegmentationPipeline
    from .fasttext_sequence_classification_pipeline import FasttextSequenceClassificationPipeline
    from .faq_question_answering_pipeline import FaqQuestionAnsweringPipeline
    from .feature_extraction_pipeline import FeatureExtractionPipeline
    from .fill_mask_pipeline import FillMaskPipeline
    from .information_extraction_pipeline import InformationExtractionPipeline
    from .named_entity_recognition_pipeline import NamedEntityRecognitionPipeline, \
        NamedEntityRecognitionThaiPipeline, \
        NamedEntityRecognitionVietPipeline
    from .text_ranking_pipeline import TextRankingPipeline
    from .sentence_embedding_pipeline import SentenceEmbeddingPipeline
    from .text_classification_pipeline import TextClassificationPipeline
    from .summarization_pipeline import SummarizationPipeline
    from .translation_quality_estimation_pipeline import TranslationQualityEstimationPipeline
    from .text_error_correction_pipeline import TextErrorCorrectionPipeline
    from .text_generation_pipeline import TextGenerationPipeline
    from .text2text_generation_pipeline import Text2TextGenerationPipeline
    from .token_classification_pipeline import TokenClassificationPipeline
    from .translation_pipeline import TranslationPipeline
    from .word_segmentation_pipeline import WordSegmentationPipeline
    from .zero_shot_classification_pipeline import ZeroShotClassificationPipeline
    from .mglm_text_summarization_pipeline import MGLMTextSummarizationPipeline
    from .multilingual_word_segmentation_pipeline import MultilingualWordSegmentationPipeline, \
        WordSegmentationThaiPipeline

else:
    _import_structure = {
        'automatic_post_editing_pipeline': ['AutomaticPostEditingPipeline'],
        'conversational_text_to_sql_pipeline':
        ['ConversationalTextToSqlPipeline'],
        'dialog_intent_prediction_pipeline':
        ['DialogIntentPredictionPipeline'],
        'dialog_modeling_pipeline': ['DialogModelingPipeline'],
        'dialog_state_tracking_pipeline': ['DialogStateTrackingPipeline'],
        'domain_classification_pipeline':
        ['FasttextSequenceClassificationPipeline'],
        'document_segmentation_pipeline': ['DocumentSegmentationPipeline'],
        'faq_question_answering_pipeline': ['FaqQuestionAnsweringPipeline'],
        'feature_extraction_pipeline': ['FeatureExtractionPipeline'],
        'fill_mask_pipeline': ['FillMaskPipeline'],
        'information_extraction_pipeline': ['InformationExtractionPipeline'],
        'named_entity_recognition_pipeline': [
            'NamedEntityRecognitionPipeline',
            'NamedEntityRecognitionThaiPipeline',
            'NamedEntityRecognitionVietPipeline'
        ],
        'text_ranking_pipeline': ['TextRankingPipeline'],
        'sentence_embedding_pipeline': ['SentenceEmbeddingPipeline'],
        'summarization_pipeline': ['SummarizationPipeline'],
        'table_question_answering_pipeline':
        ['TableQuestionAnsweringPipeline'],
        'text_classification_pipeline': ['TextClassificationPipeline'],
        'text_error_correction_pipeline': ['TextErrorCorrectionPipeline'],
        'text_generation_pipeline': ['TextGenerationPipeline'],
        'text2text_generation_pipeline': ['Text2TextGenerationPipeline'],
        'token_classification_pipeline': ['TokenClassificationPipeline'],
        'translation_pipeline': ['TranslationPipeline'],
        'translation_quality_estimation_pipeline':
        ['TranslationQualityEstimationPipeline'],
        'word_segmentation_pipeline': ['WordSegmentationPipeline'],
        'zero_shot_classification_pipeline':
        ['ZeroShotClassificationPipeline'],
        'mglm_text_summarization_pipeline': ['MGLMTextSummarizationPipeline'],
        'multilingual_word_segmentation_pipeline': [
            'MultilingualWordSegmentationPipeline',
            'WordSegmentationThaiPipeline'
        ],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
