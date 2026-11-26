"""Contains all the data models used in inputs/outputs"""

from .account_quota_state import AccountQuotaState
from .account_quota_state_quota_source import AccountQuotaStateQuotaSource
from .activity_type import ActivityType
from .add_excluded_media_body import AddExcludedMediaBody
from .add_favorite_media_body import AddFavoriteMediaBody
from .add_segment_to_collection_request import AddSegmentToCollectionRequest
from .admin_content_request import AdminContentRequest
from .admin_content_request_external_source_type_1 import AdminContentRequestExternalSourceType1
from .admin_content_request_external_source_type_2_type_1 import (
    AdminContentRequestExternalSourceType2Type1,
)
from .admin_content_request_external_source_type_3_type_1 import (
    AdminContentRequestExternalSourceType3Type1,
)
from .admin_content_request_possible_duplicate_of_type_0 import (
    AdminContentRequestPossibleDuplicateOfType0,
)
from .admin_content_request_possible_duplicate_of_type_0_status import (
    AdminContentRequestPossibleDuplicateOfType0Status,
)
from .admin_content_request_requester_type_0 import AdminContentRequestRequesterType0
from .admin_email_event import AdminEmailEvent
from .admin_email_send import AdminEmailSend
from .admin_email_send_source import AdminEmailSendSource
from .admin_email_send_status import AdminEmailSendStatus
from .admin_email_suppression import AdminEmailSuppression
from .admin_email_suppression_cause import AdminEmailSuppressionCause
from .admin_overview import AdminOverview
from .admin_overview_announcement import AdminOverviewAnnouncement
from .admin_overview_emails import AdminOverviewEmails
from .admin_overview_reports import AdminOverviewReports
from .admin_overview_requests import AdminOverviewRequests
from .admin_overview_users import AdminOverviewUsers
from .admin_patreon_campaign_member import AdminPatreonCampaignMember
from .admin_patreon_connection import AdminPatreonConnection
from .admin_patreon_connection_quota_source import AdminPatreonConnectionQuotaSource
from .admin_patreon_overview import AdminPatreonOverview
from .admin_patreon_overview_campaign import AdminPatreonOverviewCampaign
from .admin_patreon_overview_campaign_status import AdminPatreonOverviewCampaignStatus
from .admin_patreon_overview_manual_grants_item import AdminPatreonOverviewManualGrantsItem
from .admin_patreon_overview_manual_grants_item_quota_source import (
    AdminPatreonOverviewManualGrantsItemQuotaSource,
)
from .admin_patreon_overview_summary import AdminPatreonOverviewSummary
from .admin_patreon_overview_tiers_item import AdminPatreonOverviewTiersItem
from .admin_report_group import AdminReportGroup
from .admin_report_group_item import AdminReportGroupItem
from .admin_report_list_response import AdminReportListResponse
from .admin_user_with_providers import AdminUserWithProviders
from .admin_user_with_providers_role import AdminUserWithProvidersRole
from .affected_count_response import AffectedCountResponse
from .announcement import Announcement
from .announcement_type import AnnouncementType
from .api_key_scope import ApiKeyScope
from .batch_update_reports_request import BatchUpdateReportsRequest
from .bulk_delete_reports_request import BulkDeleteReportsRequest
from .bulk_delete_reports_request_filters import BulkDeleteReportsRequestFilters
from .bulk_update_reports_request import BulkUpdateReportsRequest
from .bulk_update_reports_request_filters import BulkUpdateReportsRequestFilters
from .category import Category
from .category_count import CategoryCount
from .check_word_watch_match_mode import CheckWordWatchMatchMode
from .check_word_watch_response_200 import CheckWordWatchResponse200
from .collection import Collection
from .collection_create_request import CollectionCreateRequest
from .collection_list_response import CollectionListResponse
from .collection_type import CollectionType
from .collection_update_request import CollectionUpdateRequest
from .collection_visibility import CollectionVisibility
from .complete_patreon_link_body import CompletePatreonLinkBody
from .complete_patreon_link_response_200 import CompletePatreonLinkResponse200
from .complete_tracker_link_body import CompleteTrackerLinkBody
from .complete_tracker_link_body_provider import CompleteTrackerLinkBodyProvider
from .content_rating import ContentRating
from .content_request import ContentRequest
from .content_request_category import ContentRequestCategory
from .content_request_kind import ContentRequestKind
from .content_request_media_type_0 import ContentRequestMediaType0
from .content_request_status import ContentRequestStatus
from .covered_word import CoveredWord
from .covered_words_response import CoveredWordsResponse
from .covered_words_response_tier_stats import CoveredWordsResponseTierStats
from .covered_words_update_request import CoveredWordsUpdateRequest
from .covered_words_update_response import CoveredWordsUpdateResponse
from .create_content_request_body import CreateContentRequestBody
from .create_content_request_response_200 import CreateContentRequestResponse200
from .create_content_request_response_200_outcome import CreateContentRequestResponse200Outcome
from .create_content_request_response_201 import CreateContentRequestResponse201
from .create_content_request_response_201_outcome import CreateContentRequestResponse201Outcome
from .create_feedback_request import CreateFeedbackRequest
from .create_report_request import CreateReportRequest
from .create_report_request_reason import CreateReportRequestReason
from .create_segments_batch_response_201 import CreateSegmentsBatchResponse201
from .create_user_api_key_body import CreateUserApiKeyBody
from .create_user_api_key_response_201 import CreateUserApiKeyResponse201
from .cursor_pagination import CursorPagination
from .delete_user_dictionary_response_200 import DeleteUserDictionaryResponse200
from .dictionary_candidate import DictionaryCandidate
from .dictionary_candidate_custom_frequencies_item import DictionaryCandidateCustomFrequenciesItem
from .dictionary_candidate_entries_item import DictionaryCandidateEntriesItem
from .dictionary_candidate_entries_item_senses_item import DictionaryCandidateEntriesItemSensesItem
from .dictionary_candidate_entries_item_senses_item_definitions_item import (
    DictionaryCandidateEntriesItemSensesItemDefinitionsItem,
)
from .dictionary_candidate_entries_item_senses_item_definitions_item_lang import (
    DictionaryCandidateEntriesItemSensesItemDefinitionsItemLang,
)
from .dictionary_candidate_entries_item_senses_item_tags_item import (
    DictionaryCandidateEntriesItemSensesItemTagsItem,
)
from .dictionary_candidate_entries_item_senses_item_tags_item_category import (
    DictionaryCandidateEntriesItemSensesItemTagsItemCategory,
)
from .dictionary_candidate_forms_item import DictionaryCandidateFormsItem
from .dictionary_candidate_forms_item_script import DictionaryCandidateFormsItemScript
from .dictionary_candidate_frequency_by_category_item import (
    DictionaryCandidateFrequencyByCategoryItem,
)
from .dictionary_candidate_frequency_by_category_item_category import (
    DictionaryCandidateFrequencyByCategoryItemCategory,
)
from .dictionary_candidate_furigana_item import DictionaryCandidateFuriganaItem
from .dictionary_candidate_parts_item import DictionaryCandidatePartsItem
from .dictionary_candidate_pitch_item import DictionaryCandidatePitchItem
from .dictionary_kanji import DictionaryKanji
from .dictionary_kanji_components_item import DictionaryKanjiComponentsItem
from .dictionary_kanji_meanings_language import DictionaryKanjiMeaningsLanguage
from .dictionary_kanji_radical_type_0 import DictionaryKanjiRadicalType0
from .dictionary_kanji_readings_item import DictionaryKanjiReadingsItem
from .dictionary_kanji_readings_item_examples_item import DictionaryKanjiReadingsItemExamplesItem
from .dictionary_kanji_readings_item_examples_item_furigana_item import (
    DictionaryKanjiReadingsItemExamplesItemFuriganaItem,
)
from .dictionary_kanji_readings_item_kind import DictionaryKanjiReadingsItemKind
from .dictionary_kanji_related import DictionaryKanjiRelated
from .dictionary_kanji_word_ref import DictionaryKanjiWordRef
from .dictionary_kanji_words_item import DictionaryKanjiWordsItem
from .episode import Episode
from .episode_create_request import EpisodeCreateRequest
from .episode_list_response import EpisodeListResponse
from .episode_update_request import EpisodeUpdateRequest
from .error_400 import Error400
from .error_400_code import Error400Code
from .error_400_errors import Error400Errors
from .error_400_status import Error400Status
from .error_401 import Error401
from .error_401_code import Error401Code
from .error_401_errors import Error401Errors
from .error_401_status import Error401Status
from .error_403 import Error403
from .error_403_code import Error403Code
from .error_403_errors import Error403Errors
from .error_403_status import Error403Status
from .error_404 import Error404
from .error_404_code import Error404Code
from .error_404_errors import Error404Errors
from .error_404_status import Error404Status
from .error_409 import Error409
from .error_409_code import Error409Code
from .error_409_errors import Error409Errors
from .error_409_status import Error409Status
from .error_429 import Error429
from .error_429_code import Error429Code
from .error_429_errors import Error429Errors
from .error_429_status import Error429Status
from .error_500 import Error500
from .error_500_code import Error500Code
from .error_500_errors import Error500Errors
from .error_500_status import Error500Status
from .error_503 import Error503
from .error_503_code import Error503Code
from .error_503_errors import Error503Errors
from .error_503_status import Error503Status
from .external_id import ExternalId
from .feedback_form_token import FeedbackFormToken
from .feedback_receipt import FeedbackReceipt
from .get_admin_email_response_200 import GetAdminEmailResponse200
from .get_admin_users_with_providers_response_200 import GetAdminUsersWithProvidersResponse200
from .get_content_request_allowance_response_200 import GetContentRequestAllowanceResponse200
from .get_content_request_allowance_response_200_boosts import (
    GetContentRequestAllowanceResponse200Boosts,
)
from .get_covered_words_filter import GetCoveredWordsFilter
from .get_dictionary_kanji_index_locale import GetDictionaryKanjiIndexLocale
from .get_dictionary_kanji_index_response_200 import GetDictionaryKanjiIndexResponse200
from .get_dictionary_kanji_index_response_200_kanji_item import (
    GetDictionaryKanjiIndexResponse200KanjiItem,
)
from .get_dictionary_kanji_locale import GetDictionaryKanjiLocale
from .get_dictionary_kanji_related import GetDictionaryKanjiRelated
from .get_email_preferences_by_token_response_200 import GetEmailPreferencesByTokenResponse200
from .get_email_preferences_by_token_response_200_categories import (
    GetEmailPreferencesByTokenResponse200Categories,
)
from .get_email_preferences_by_token_response_200_category import (
    GetEmailPreferencesByTokenResponse200Category,
)
from .get_patreon_connection_response_200 import GetPatreonConnectionResponse200
from .get_unread_notification_count_response_200 import GetUnreadNotificationCountResponse200
from .get_user_activity_heatmap_response_200 import GetUserActivityHeatmapResponse200
from .get_user_activity_heatmap_response_200_activity_by_day import (
    GetUserActivityHeatmapResponse200ActivityByDay,
)
from .heatmap_day_counts import HeatmapDayCounts
from .identify_dictionary_word_locale import IdentifyDictionaryWordLocale
from .identify_dictionary_word_response_200 import IdentifyDictionaryWordResponse200
from .include_expansion import IncludeExpansion
from .lift_admin_email_suppression_body import LiftAdminEmailSuppressionBody
from .list_admin_content_requests_category import ListAdminContentRequestsCategory
from .list_admin_content_requests_response_200 import ListAdminContentRequestsResponse200
from .list_admin_content_requests_status import ListAdminContentRequestsStatus
from .list_admin_email_suppressions_response_200 import ListAdminEmailSuppressionsResponse200
from .list_admin_emails_response_200 import ListAdminEmailsResponse200
from .list_admin_emails_response_200_last_24h import ListAdminEmailsResponse200Last24H
from .list_admin_emails_status import ListAdminEmailsStatus
from .list_content_requests_category import ListContentRequestsCategory
from .list_content_requests_response_200 import ListContentRequestsResponse200
from .list_content_requests_sort import ListContentRequestsSort
from .list_content_requests_status import ListContentRequestsStatus
from .list_excluded_media_response_200 import ListExcludedMediaResponse200
from .list_familiar_media_response_200 import ListFamiliarMediaResponse200
from .list_familiar_media_response_200_familiar_media_item import (
    ListFamiliarMediaResponse200FamiliarMediaItem,
)
from .list_favorite_media_response_200 import ListFavoriteMediaResponse200
from .list_media_category import ListMediaCategory
from .list_my_content_requests_category import ListMyContentRequestsCategory
from .list_my_content_requests_response_200 import ListMyContentRequestsResponse200
from .list_my_content_requests_scope import ListMyContentRequestsScope
from .list_my_content_requests_sort import ListMyContentRequestsSort
from .list_my_content_requests_status import ListMyContentRequestsStatus
from .list_notifications_response_200 import ListNotificationsResponse200
from .list_segment_revisions_response_200 import ListSegmentRevisionsResponse200
from .list_tiers_response_200 import ListTiersResponse200
from .list_user_activity_response_200 import ListUserActivityResponse200
from .list_word_watches_response_200 import ListWordWatchesResponse200
from .mark_notifications_read_body import MarkNotificationsReadBody
from .mark_notifications_read_response_200 import MarkNotificationsReadResponse200
from .media import Media
from .media_airing_format import MediaAiringFormat
from .media_airing_status import MediaAiringStatus
from .media_autocomplete_response import MediaAutocompleteResponse
from .media_create_request import MediaCreateRequest
from .media_create_request_airing_format import MediaCreateRequestAiringFormat
from .media_create_request_airing_status import MediaCreateRequestAiringStatus
from .media_create_request_season_name import MediaCreateRequestSeasonName
from .media_create_request_storage import MediaCreateRequestStorage
from .media_filter_item import MediaFilterItem
from .media_global_stats import MediaGlobalStats
from .media_list_response import MediaListResponse
from .media_search_stats import MediaSearchStats
from .media_search_stats_episode_hits_item import MediaSearchStatsEpisodeHitsItem
from .media_season_name import MediaSeasonName
from .media_summary import MediaSummary
from .media_update_request import MediaUpdateRequest
from .media_update_request_airing_format import MediaUpdateRequestAiringFormat
from .media_update_request_airing_status import MediaUpdateRequestAiringStatus
from .media_update_request_season_name import MediaUpdateRequestSeasonName
from .media_update_request_storage import MediaUpdateRequestStorage
from .merge_admin_content_request_body import MergeAdminContentRequestBody
from .moderate_episode_segments_request import ModerateEpisodeSegmentsRequest
from .moderate_episode_segments_request_action import ModerateEpisodeSegmentsRequestAction
from .notification import Notification
from .notification_kind import NotificationKind
from .notification_payload import NotificationPayload
from .patreon_connection import PatreonConnection
from .preview_content_request_body import PreviewContentRequestBody
from .preview_content_request_response_200 import PreviewContentRequestResponse200
from .preview_content_request_response_200_category import PreviewContentRequestResponse200Category
from .preview_content_request_response_200_existing_type_0 import (
    PreviewContentRequestResponse200ExistingType0,
)
from .preview_content_request_response_200_existing_type_0_media import (
    PreviewContentRequestResponse200ExistingType0Media,
)
from .refresh_all_admin_patreon_connections_response_200 import (
    RefreshAllAdminPatreonConnectionsResponse200,
)
from .report import Report
from .report_data_type_0 import ReportDataType0
from .report_reason import ReportReason
from .report_source import ReportSource
from .report_status import ReportStatus
from .report_target_episode import ReportTargetEpisode
from .report_target_episode_type import ReportTargetEpisodeType
from .report_target_media import ReportTargetMedia
from .report_target_media_type import ReportTargetMediaType
from .report_target_segment import ReportTargetSegment
from .report_target_segment_input import ReportTargetSegmentInput
from .report_target_segment_input_type import ReportTargetSegmentInputType
from .report_target_segment_type import ReportTargetSegmentType
from .report_target_type import ReportTargetType
from .reserve_user_dictionary_upload_body import ReserveUserDictionaryUploadBody
from .reserve_user_dictionary_upload_response_201 import ReserveUserDictionaryUploadResponse201
from .reserve_user_dictionary_upload_response_201_headers import (
    ReserveUserDictionaryUploadResponse201Headers,
)
from .reserve_user_dictionary_upload_response_201_method import (
    ReserveUserDictionaryUploadResponse201Method,
)
from .search_filters import SearchFilters
from .search_filters_languages_type_0_item import SearchFiltersLanguagesType0Item
from .search_filters_languages_type_1 import SearchFiltersLanguagesType1
from .search_filters_languages_type_1_exclude_item import SearchFiltersLanguagesType1ExcludeItem
from .search_filters_media import SearchFiltersMedia
from .search_filters_segment_duration_ms import SearchFiltersSegmentDurationMs
from .search_filters_segment_length_chars import SearchFiltersSegmentLengthChars
from .search_media_filters import SearchMediaFilters
from .search_media_request import SearchMediaRequest
from .search_multiple_query import SearchMultipleQuery
from .search_multiple_query_match_mode import SearchMultipleQueryMatchMode
from .search_multiple_request import SearchMultipleRequest
from .search_multiple_response import SearchMultipleResponse
from .search_multiple_response_includes import SearchMultipleResponseIncludes
from .search_multiple_response_includes_media import SearchMultipleResponseIncludesMedia
from .search_pagination import SearchPagination
from .search_pagination_estimated_total_hits_relation import (
    SearchPaginationEstimatedTotalHitsRelation,
)
from .search_query import SearchQuery
from .search_query_match_mode import SearchQueryMatchMode
from .search_request import SearchRequest
from .search_response import SearchResponse
from .search_response_includes import SearchResponseIncludes
from .search_response_includes_media import SearchResponseIncludesMedia
from .search_sort import SearchSort
from .search_sort_mode import SearchSortMode
from .search_stats_request import SearchStatsRequest
from .search_stats_response import SearchStatsResponse
from .search_stats_response_includes import SearchStatsResponseIncludes
from .search_stats_response_includes_media import SearchStatsResponseIncludesMedia
from .segment import Segment
from .segment_batch_create_request import SegmentBatchCreateRequest
from .segment_context_response import SegmentContextResponse
from .segment_context_response_includes import SegmentContextResponseIncludes
from .segment_context_response_includes_media import SegmentContextResponseIncludesMedia
from .segment_create_request import SegmentCreateRequest
from .segment_create_request_rating_analysis_type_0 import SegmentCreateRequestRatingAnalysisType0
from .segment_create_request_storage import SegmentCreateRequestStorage
from .segment_create_request_text_en import SegmentCreateRequestTextEn
from .segment_create_request_text_es import SegmentCreateRequestTextEs
from .segment_create_request_text_ja import SegmentCreateRequestTextJa
from .segment_internal import SegmentInternal
from .segment_internal_rating_analysis_type_0 import SegmentInternalRatingAnalysisType0
from .segment_internal_storage import SegmentInternalStorage
from .segment_list_response import SegmentListResponse
from .segment_revision import SegmentRevision
from .segment_revision_actor import SegmentRevisionActor
from .segment_revision_snapshot import SegmentRevisionSnapshot
from .segment_status import SegmentStatus
from .segment_text_en import SegmentTextEn
from .segment_text_es import SegmentTextEs
from .segment_text_ja import SegmentTextJa
from .segment_update_request import SegmentUpdateRequest
from .segment_update_request_rating_analysis_type_0 import SegmentUpdateRequestRatingAnalysisType0
from .segment_update_request_storage import SegmentUpdateRequestStorage
from .segment_update_request_text_en import SegmentUpdateRequestTextEn
from .segment_update_request_text_es import SegmentUpdateRequestTextEs
from .segment_update_request_text_ja import SegmentUpdateRequestTextJa
from .segment_urls import SegmentUrls
from .set_word_watch_body import SetWordWatchBody
from .set_word_watch_body_match_mode import SetWordWatchBodyMatchMode
from .set_word_watch_body_mode import SetWordWatchBodyMode
from .start_patreon_link_response_201 import StartPatreonLinkResponse201
from .start_tracker_link_body import StartTrackerLinkBody
from .start_tracker_link_body_provider import StartTrackerLinkBodyProvider
from .start_tracker_link_response_201 import StartTrackerLinkResponse201
from .stats_overview import StatsOverview
from .stats_overview_translations import StatsOverviewTranslations
from .tier import Tier
from .token import Token
from .token_f_item import TokenFItem
from .token_inflection import TokenInflection
from .token_kind import TokenKind
from .token_parts_item import TokenPartsItem
from .tracker_state import TrackerState
from .tracker_state_configured_providers_item import TrackerStateConfiguredProvidersItem
from .tracker_state_connection_type_0 import TrackerStateConnectionType0
from .tracker_state_connection_type_0_effective_settings import (
    TrackerStateConnectionType0EffectiveSettings,
)
from .tracker_state_connection_type_0_provider import TrackerStateConnectionType0Provider
from .tracker_state_connection_type_0_settings import TrackerStateConnectionType0Settings
from .tracker_state_coverage_type_0 import TrackerStateCoverageType0
from .tracker_state_coverage_type_0_by_status import TrackerStateCoverageType0ByStatus
from .tracker_state_entries_item import TrackerStateEntriesItem
from .tracker_state_entries_item_status import TrackerStateEntriesItemStatus
from .tracker_state_missing_anime_item import TrackerStateMissingAnimeItem
from .tracker_state_missing_anime_item_external_source import (
    TrackerStateMissingAnimeItemExternalSource,
)
from .tracker_state_missing_anime_item_request_type_0 import (
    TrackerStateMissingAnimeItemRequestType0,
)
from .tracker_state_missing_anime_item_request_type_0_status import (
    TrackerStateMissingAnimeItemRequestType0Status,
)
from .tracker_state_missing_anime_item_status import TrackerStateMissingAnimeItemStatus
from .unsubscribe_receipt import UnsubscribeReceipt
from .update_account_quota_request import UpdateAccountQuotaRequest
from .update_admin_content_request_body import UpdateAdminContentRequestBody
from .update_admin_content_request_body_category import UpdateAdminContentRequestBodyCategory
from .update_admin_content_request_body_kind import UpdateAdminContentRequestBodyKind
from .update_admin_content_request_body_status import UpdateAdminContentRequestBodyStatus
from .update_collection_segment_request import UpdateCollectionSegmentRequest
from .update_email_preferences_by_token_body import UpdateEmailPreferencesByTokenBody
from .update_email_preferences_by_token_response_200 import UpdateEmailPreferencesByTokenResponse200
from .update_email_preferences_by_token_response_200_categories import (
    UpdateEmailPreferencesByTokenResponse200Categories,
)
from .update_report_request import UpdateReportRequest
from .update_tracker_settings_body import UpdateTrackerSettingsBody
from .update_user_dictionaries_body import UpdateUserDictionariesBody
from .update_user_dictionaries_body_items_item import UpdateUserDictionariesBodyItemsItem
from .update_word_watch_body import UpdateWordWatchBody
from .update_word_watch_body_mode import UpdateWordWatchBodyMode
from .user_activity import UserActivity
from .user_activity_request import UserActivityRequest
from .user_activity_request_activity_type import UserActivityRequestActivityType
from .user_activity_stats import UserActivityStats
from .user_activity_stats_top_media_item import UserActivityStatsTopMediaItem
from .user_dictionary import UserDictionary
from .user_dictionary_list_response import UserDictionaryListResponse
from .user_dictionary_list_response_builtin import UserDictionaryListResponseBuiltin
from .user_dictionary_list_response_quota import UserDictionaryListResponseQuota
from .user_dictionary_status import UserDictionaryStatus
from .user_dictionary_upload_result import UserDictionaryUploadResult
from .user_export_collection import UserExportCollection
from .user_export_response import UserExportResponse
from .user_export_response_media_affinity_item import UserExportResponseMediaAffinityItem
from .user_export_response_profile import UserExportResponseProfile
from .user_export_response_truncated import UserExportResponseTruncated
from .user_me import UserMe
from .user_me_quota import UserMeQuota
from .user_me_quota_burst import UserMeQuotaBurst
from .user_me_quota_tier_type_0 import UserMeQuotaTierType0
from .user_me_user import UserMeUser
from .user_preferences import UserPreferences
from .user_preferences_anki_profiles_item import UserPreferencesAnkiProfilesItem
from .user_preferences_anki_profiles_item_fields_item import (
    UserPreferencesAnkiProfilesItemFieldsItem,
)
from .user_preferences_content_rating_preferences import UserPreferencesContentRatingPreferences
from .user_preferences_content_rating_preferences_nsfw import (
    UserPreferencesContentRatingPreferencesNsfw,
)
from .user_preferences_custom_theme_type_0 import UserPreferencesCustomThemeType0
from .user_preferences_custom_theme_type_0_base import UserPreferencesCustomThemeType0Base
from .user_preferences_custom_theme_type_0_preset import UserPreferencesCustomThemeType0Preset
from .user_preferences_default_search_category import UserPreferencesDefaultSearchCategory
from .user_preferences_familiar_media import UserPreferencesFamiliarMedia
from .user_preferences_favorite_media_item import UserPreferencesFavoriteMediaItem
from .user_preferences_hidden_media_item import UserPreferencesHiddenMediaItem
from .user_preferences_media_card_default import UserPreferencesMediaCardDefault
from .user_preferences_media_name_language import UserPreferencesMediaNameLanguage
from .user_preferences_product_emails import UserPreferencesProductEmails
from .user_preferences_search_history import UserPreferencesSearchHistory
from .user_preferences_site_notifications import UserPreferencesSiteNotifications
from .user_preferences_translation_languages_item import UserPreferencesTranslationLanguagesItem
from .user_preferences_translation_visibility_preferences import (
    UserPreferencesTranslationVisibilityPreferences,
)
from .user_preferences_translation_visibility_preferences_en import (
    UserPreferencesTranslationVisibilityPreferencesEN,
)
from .user_preferences_translation_visibility_preferences_es import (
    UserPreferencesTranslationVisibilityPreferencesES,
)
from .user_preferences_word_popup import UserPreferencesWordPopup
from .user_preferences_word_popup_definition_size import UserPreferencesWordPopupDefinitionSize
from .word_coverage_tier import WordCoverageTier
from .word_match import WordMatch
from .word_match_media import WordMatchMedia
from .word_watch import WordWatch
from .word_watch_match_mode import WordWatchMatchMode
from .word_watch_mode import WordWatchMode
from .word_watch_set_response import WordWatchSetResponse
from .word_watch_set_response_outcome import WordWatchSetResponseOutcome
from .word_watch_status import WordWatchStatus

__all__ = (
    "AccountQuotaState",
    "AccountQuotaStateQuotaSource",
    "ActivityType",
    "AddExcludedMediaBody",
    "AddFavoriteMediaBody",
    "AddSegmentToCollectionRequest",
    "AdminContentRequest",
    "AdminContentRequestExternalSourceType1",
    "AdminContentRequestExternalSourceType2Type1",
    "AdminContentRequestExternalSourceType3Type1",
    "AdminContentRequestPossibleDuplicateOfType0",
    "AdminContentRequestPossibleDuplicateOfType0Status",
    "AdminContentRequestRequesterType0",
    "AdminEmailEvent",
    "AdminEmailSend",
    "AdminEmailSendSource",
    "AdminEmailSendStatus",
    "AdminEmailSuppression",
    "AdminEmailSuppressionCause",
    "AdminOverview",
    "AdminOverviewAnnouncement",
    "AdminOverviewEmails",
    "AdminOverviewReports",
    "AdminOverviewRequests",
    "AdminOverviewUsers",
    "AdminPatreonCampaignMember",
    "AdminPatreonConnection",
    "AdminPatreonConnectionQuotaSource",
    "AdminPatreonOverview",
    "AdminPatreonOverviewCampaign",
    "AdminPatreonOverviewCampaignStatus",
    "AdminPatreonOverviewManualGrantsItem",
    "AdminPatreonOverviewManualGrantsItemQuotaSource",
    "AdminPatreonOverviewSummary",
    "AdminPatreonOverviewTiersItem",
    "AdminReportGroup",
    "AdminReportGroupItem",
    "AdminReportListResponse",
    "AdminUserWithProviders",
    "AdminUserWithProvidersRole",
    "AffectedCountResponse",
    "Announcement",
    "AnnouncementType",
    "ApiKeyScope",
    "BatchUpdateReportsRequest",
    "BulkDeleteReportsRequest",
    "BulkDeleteReportsRequestFilters",
    "BulkUpdateReportsRequest",
    "BulkUpdateReportsRequestFilters",
    "Category",
    "CategoryCount",
    "CheckWordWatchMatchMode",
    "CheckWordWatchResponse200",
    "Collection",
    "CollectionCreateRequest",
    "CollectionListResponse",
    "CollectionType",
    "CollectionUpdateRequest",
    "CollectionVisibility",
    "CompletePatreonLinkBody",
    "CompletePatreonLinkResponse200",
    "CompleteTrackerLinkBody",
    "CompleteTrackerLinkBodyProvider",
    "ContentRating",
    "ContentRequest",
    "ContentRequestCategory",
    "ContentRequestKind",
    "ContentRequestMediaType0",
    "ContentRequestStatus",
    "CoveredWord",
    "CoveredWordsResponse",
    "CoveredWordsResponseTierStats",
    "CoveredWordsUpdateRequest",
    "CoveredWordsUpdateResponse",
    "CreateContentRequestBody",
    "CreateContentRequestResponse200",
    "CreateContentRequestResponse200Outcome",
    "CreateContentRequestResponse201",
    "CreateContentRequestResponse201Outcome",
    "CreateFeedbackRequest",
    "CreateReportRequest",
    "CreateReportRequestReason",
    "CreateSegmentsBatchResponse201",
    "CreateUserApiKeyBody",
    "CreateUserApiKeyResponse201",
    "CursorPagination",
    "DeleteUserDictionaryResponse200",
    "DictionaryCandidate",
    "DictionaryCandidateCustomFrequenciesItem",
    "DictionaryCandidateEntriesItem",
    "DictionaryCandidateEntriesItemSensesItem",
    "DictionaryCandidateEntriesItemSensesItemDefinitionsItem",
    "DictionaryCandidateEntriesItemSensesItemDefinitionsItemLang",
    "DictionaryCandidateEntriesItemSensesItemTagsItem",
    "DictionaryCandidateEntriesItemSensesItemTagsItemCategory",
    "DictionaryCandidateFormsItem",
    "DictionaryCandidateFormsItemScript",
    "DictionaryCandidateFrequencyByCategoryItem",
    "DictionaryCandidateFrequencyByCategoryItemCategory",
    "DictionaryCandidateFuriganaItem",
    "DictionaryCandidatePartsItem",
    "DictionaryCandidatePitchItem",
    "DictionaryKanji",
    "DictionaryKanjiComponentsItem",
    "DictionaryKanjiMeaningsLanguage",
    "DictionaryKanjiRadicalType0",
    "DictionaryKanjiReadingsItem",
    "DictionaryKanjiReadingsItemExamplesItem",
    "DictionaryKanjiReadingsItemExamplesItemFuriganaItem",
    "DictionaryKanjiReadingsItemKind",
    "DictionaryKanjiRelated",
    "DictionaryKanjiWordRef",
    "DictionaryKanjiWordsItem",
    "Episode",
    "EpisodeCreateRequest",
    "EpisodeListResponse",
    "EpisodeUpdateRequest",
    "Error400",
    "Error400Code",
    "Error400Errors",
    "Error400Status",
    "Error401",
    "Error401Code",
    "Error401Errors",
    "Error401Status",
    "Error403",
    "Error403Code",
    "Error403Errors",
    "Error403Status",
    "Error404",
    "Error404Code",
    "Error404Errors",
    "Error404Status",
    "Error409",
    "Error409Code",
    "Error409Errors",
    "Error409Status",
    "Error429",
    "Error429Code",
    "Error429Errors",
    "Error429Status",
    "Error500",
    "Error500Code",
    "Error500Errors",
    "Error500Status",
    "Error503",
    "Error503Code",
    "Error503Errors",
    "Error503Status",
    "ExternalId",
    "FeedbackFormToken",
    "FeedbackReceipt",
    "GetAdminEmailResponse200",
    "GetAdminUsersWithProvidersResponse200",
    "GetContentRequestAllowanceResponse200",
    "GetContentRequestAllowanceResponse200Boosts",
    "GetCoveredWordsFilter",
    "GetDictionaryKanjiIndexLocale",
    "GetDictionaryKanjiIndexResponse200",
    "GetDictionaryKanjiIndexResponse200KanjiItem",
    "GetDictionaryKanjiLocale",
    "GetDictionaryKanjiRelated",
    "GetEmailPreferencesByTokenResponse200",
    "GetEmailPreferencesByTokenResponse200Categories",
    "GetEmailPreferencesByTokenResponse200Category",
    "GetPatreonConnectionResponse200",
    "GetUnreadNotificationCountResponse200",
    "GetUserActivityHeatmapResponse200",
    "GetUserActivityHeatmapResponse200ActivityByDay",
    "HeatmapDayCounts",
    "IdentifyDictionaryWordLocale",
    "IdentifyDictionaryWordResponse200",
    "IncludeExpansion",
    "LiftAdminEmailSuppressionBody",
    "ListAdminContentRequestsCategory",
    "ListAdminContentRequestsResponse200",
    "ListAdminContentRequestsStatus",
    "ListAdminEmailsResponse200",
    "ListAdminEmailsResponse200Last24H",
    "ListAdminEmailsStatus",
    "ListAdminEmailSuppressionsResponse200",
    "ListContentRequestsCategory",
    "ListContentRequestsResponse200",
    "ListContentRequestsSort",
    "ListContentRequestsStatus",
    "ListExcludedMediaResponse200",
    "ListFamiliarMediaResponse200",
    "ListFamiliarMediaResponse200FamiliarMediaItem",
    "ListFavoriteMediaResponse200",
    "ListMediaCategory",
    "ListMyContentRequestsCategory",
    "ListMyContentRequestsResponse200",
    "ListMyContentRequestsScope",
    "ListMyContentRequestsSort",
    "ListMyContentRequestsStatus",
    "ListNotificationsResponse200",
    "ListSegmentRevisionsResponse200",
    "ListTiersResponse200",
    "ListUserActivityResponse200",
    "ListWordWatchesResponse200",
    "MarkNotificationsReadBody",
    "MarkNotificationsReadResponse200",
    "Media",
    "MediaAiringFormat",
    "MediaAiringStatus",
    "MediaAutocompleteResponse",
    "MediaCreateRequest",
    "MediaCreateRequestAiringFormat",
    "MediaCreateRequestAiringStatus",
    "MediaCreateRequestSeasonName",
    "MediaCreateRequestStorage",
    "MediaFilterItem",
    "MediaGlobalStats",
    "MediaListResponse",
    "MediaSearchStats",
    "MediaSearchStatsEpisodeHitsItem",
    "MediaSeasonName",
    "MediaSummary",
    "MediaUpdateRequest",
    "MediaUpdateRequestAiringFormat",
    "MediaUpdateRequestAiringStatus",
    "MediaUpdateRequestSeasonName",
    "MediaUpdateRequestStorage",
    "MergeAdminContentRequestBody",
    "ModerateEpisodeSegmentsRequest",
    "ModerateEpisodeSegmentsRequestAction",
    "Notification",
    "NotificationKind",
    "NotificationPayload",
    "PatreonConnection",
    "PreviewContentRequestBody",
    "PreviewContentRequestResponse200",
    "PreviewContentRequestResponse200Category",
    "PreviewContentRequestResponse200ExistingType0",
    "PreviewContentRequestResponse200ExistingType0Media",
    "RefreshAllAdminPatreonConnectionsResponse200",
    "Report",
    "ReportDataType0",
    "ReportReason",
    "ReportSource",
    "ReportStatus",
    "ReportTargetEpisode",
    "ReportTargetEpisodeType",
    "ReportTargetMedia",
    "ReportTargetMediaType",
    "ReportTargetSegment",
    "ReportTargetSegmentInput",
    "ReportTargetSegmentInputType",
    "ReportTargetSegmentType",
    "ReportTargetType",
    "ReserveUserDictionaryUploadBody",
    "ReserveUserDictionaryUploadResponse201",
    "ReserveUserDictionaryUploadResponse201Headers",
    "ReserveUserDictionaryUploadResponse201Method",
    "SearchFilters",
    "SearchFiltersLanguagesType0Item",
    "SearchFiltersLanguagesType1",
    "SearchFiltersLanguagesType1ExcludeItem",
    "SearchFiltersMedia",
    "SearchFiltersSegmentDurationMs",
    "SearchFiltersSegmentLengthChars",
    "SearchMediaFilters",
    "SearchMediaRequest",
    "SearchMultipleQuery",
    "SearchMultipleQueryMatchMode",
    "SearchMultipleRequest",
    "SearchMultipleResponse",
    "SearchMultipleResponseIncludes",
    "SearchMultipleResponseIncludesMedia",
    "SearchPagination",
    "SearchPaginationEstimatedTotalHitsRelation",
    "SearchQuery",
    "SearchQueryMatchMode",
    "SearchRequest",
    "SearchResponse",
    "SearchResponseIncludes",
    "SearchResponseIncludesMedia",
    "SearchSort",
    "SearchSortMode",
    "SearchStatsRequest",
    "SearchStatsResponse",
    "SearchStatsResponseIncludes",
    "SearchStatsResponseIncludesMedia",
    "Segment",
    "SegmentBatchCreateRequest",
    "SegmentContextResponse",
    "SegmentContextResponseIncludes",
    "SegmentContextResponseIncludesMedia",
    "SegmentCreateRequest",
    "SegmentCreateRequestRatingAnalysisType0",
    "SegmentCreateRequestStorage",
    "SegmentCreateRequestTextEn",
    "SegmentCreateRequestTextEs",
    "SegmentCreateRequestTextJa",
    "SegmentInternal",
    "SegmentInternalRatingAnalysisType0",
    "SegmentInternalStorage",
    "SegmentListResponse",
    "SegmentRevision",
    "SegmentRevisionActor",
    "SegmentRevisionSnapshot",
    "SegmentStatus",
    "SegmentTextEn",
    "SegmentTextEs",
    "SegmentTextJa",
    "SegmentUpdateRequest",
    "SegmentUpdateRequestRatingAnalysisType0",
    "SegmentUpdateRequestStorage",
    "SegmentUpdateRequestTextEn",
    "SegmentUpdateRequestTextEs",
    "SegmentUpdateRequestTextJa",
    "SegmentUrls",
    "SetWordWatchBody",
    "SetWordWatchBodyMatchMode",
    "SetWordWatchBodyMode",
    "StartPatreonLinkResponse201",
    "StartTrackerLinkBody",
    "StartTrackerLinkBodyProvider",
    "StartTrackerLinkResponse201",
    "StatsOverview",
    "StatsOverviewTranslations",
    "Tier",
    "Token",
    "TokenFItem",
    "TokenInflection",
    "TokenKind",
    "TokenPartsItem",
    "TrackerState",
    "TrackerStateConfiguredProvidersItem",
    "TrackerStateConnectionType0",
    "TrackerStateConnectionType0EffectiveSettings",
    "TrackerStateConnectionType0Provider",
    "TrackerStateConnectionType0Settings",
    "TrackerStateCoverageType0",
    "TrackerStateCoverageType0ByStatus",
    "TrackerStateEntriesItem",
    "TrackerStateEntriesItemStatus",
    "TrackerStateMissingAnimeItem",
    "TrackerStateMissingAnimeItemExternalSource",
    "TrackerStateMissingAnimeItemRequestType0",
    "TrackerStateMissingAnimeItemRequestType0Status",
    "TrackerStateMissingAnimeItemStatus",
    "UnsubscribeReceipt",
    "UpdateAccountQuotaRequest",
    "UpdateAdminContentRequestBody",
    "UpdateAdminContentRequestBodyCategory",
    "UpdateAdminContentRequestBodyKind",
    "UpdateAdminContentRequestBodyStatus",
    "UpdateCollectionSegmentRequest",
    "UpdateEmailPreferencesByTokenBody",
    "UpdateEmailPreferencesByTokenResponse200",
    "UpdateEmailPreferencesByTokenResponse200Categories",
    "UpdateReportRequest",
    "UpdateTrackerSettingsBody",
    "UpdateUserDictionariesBody",
    "UpdateUserDictionariesBodyItemsItem",
    "UpdateWordWatchBody",
    "UpdateWordWatchBodyMode",
    "UserActivity",
    "UserActivityRequest",
    "UserActivityRequestActivityType",
    "UserActivityStats",
    "UserActivityStatsTopMediaItem",
    "UserDictionary",
    "UserDictionaryListResponse",
    "UserDictionaryListResponseBuiltin",
    "UserDictionaryListResponseQuota",
    "UserDictionaryStatus",
    "UserDictionaryUploadResult",
    "UserExportCollection",
    "UserExportResponse",
    "UserExportResponseMediaAffinityItem",
    "UserExportResponseProfile",
    "UserExportResponseTruncated",
    "UserMe",
    "UserMeQuota",
    "UserMeQuotaBurst",
    "UserMeQuotaTierType0",
    "UserMeUser",
    "UserPreferences",
    "UserPreferencesAnkiProfilesItem",
    "UserPreferencesAnkiProfilesItemFieldsItem",
    "UserPreferencesContentRatingPreferences",
    "UserPreferencesContentRatingPreferencesNsfw",
    "UserPreferencesCustomThemeType0",
    "UserPreferencesCustomThemeType0Base",
    "UserPreferencesCustomThemeType0Preset",
    "UserPreferencesDefaultSearchCategory",
    "UserPreferencesFamiliarMedia",
    "UserPreferencesFavoriteMediaItem",
    "UserPreferencesHiddenMediaItem",
    "UserPreferencesMediaCardDefault",
    "UserPreferencesMediaNameLanguage",
    "UserPreferencesProductEmails",
    "UserPreferencesSearchHistory",
    "UserPreferencesSiteNotifications",
    "UserPreferencesTranslationLanguagesItem",
    "UserPreferencesTranslationVisibilityPreferences",
    "UserPreferencesTranslationVisibilityPreferencesEN",
    "UserPreferencesTranslationVisibilityPreferencesES",
    "UserPreferencesWordPopup",
    "UserPreferencesWordPopupDefinitionSize",
    "WordCoverageTier",
    "WordMatch",
    "WordMatchMedia",
    "WordWatch",
    "WordWatchMatchMode",
    "WordWatchMode",
    "WordWatchSetResponse",
    "WordWatchSetResponseOutcome",
    "WordWatchStatus",
)
