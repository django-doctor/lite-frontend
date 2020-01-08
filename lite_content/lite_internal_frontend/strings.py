from lite_content.lite_internal_frontend import cases, letter_templates

CASES = cases
LETTER_TEMPLATES = letter_templates

# Buttons
CONTINUE = "Continue"
SAVE = "Save"
NOT_APPLICABLE = "N/A"

QUEUE_ALL_CASES = "All cases"

CASE_CHANGES = "See what has changed"

USERS_LIST_PAGE_EDIT = "Edit"

ROLES_LIST_PAGE_CREATE = "Create a new role"

USER_PROFILE_PAGE_EDIT = "Edit"
USER_DEACTIVATE = "Deactivate"
USER_REACTIVATE = "Reactivate"

# Generate Document
CHOOSE_TEMPLATE_TITLE = "Select a template"
CHOOSE_TEMPLATE_BUTTON = CONTINUE
PREVIEW_DOCUMENT_TITLE = "Preview"
PREVIEW_DOCUMENT_BUTTON = SAVE

# Organisation
ORGANISATION_CREATION_SUCCESS = "The organisation was created successfully"
ORGANISATION_SET_FLAGS = "Set flags on this organisation"
ORGANISATION_EDIT_FLAGS = "Edit organisation flags"

# HMRC Organisation
HMRC_ORGANISATION_CREATION_SUCCESS = "The HMRC organisation was created successfully"

# Flags
SET_CASE_FLAGS = "Set case flags"
EDIT_CASE_FLAGS = "Edit case flags"

# Case
CASE_GOODS = "Products"
CASE_GOODS_LOCATION = "Products location"
CASE_GOODS_LOCATION_NAME = "Name"
CASE_GOODS_LOCATION_ADDRESS = "Address"
CASE_ENTITIES_INVOLVED = "Entities involved"
CASE_ENTITIES_ACTIVITY = "Activity"
CASE_PARTIES_NAME = "Name"
CASE_PARTIES_ADDRESS = "Address"
CASE_PARTIES_TYPE = "Type"
CASE_PARTIES_WEBSITE = "Website"
CASE_PARTIES_DOCUMENT = "Document"
CASE_PARTIES_LICENSEE = "Licensee"

CASE_INFO_TYPE = "Type"
CASE_INFO_ORGANISATION = "Organisation"
CASE_INFO_STATUS = "Status"
CASE_INFO_ACTIVITY = "Activity"
CASE_INFO_SUBMITTED_AT = "Submitted at"
CASE_INFO_REFERENCE_NUMBER = "Reference number"
CASE_INFO_EXPORT_TYPE = "Export type"
CASE_INFO_USAGE = "Usage"
CASE_INFO_LAST_UPDATED = "Last updated"

CASE_COUNTRIES = "Countries"
CASE_COUNTRIES_GREEN_LIST = "Green list"
CASE_DESTINATIONS_HEADER = "Destinations"

CASE_ACTIVITY_HEADING = "Activity"

# Good
GOOD_DESCRIPTION = "Description"
GOOD_CONTROL_LIST_ENTRY = "Control list entry"
GOOD_CONTROLLED = "Controlled"
GOOD_FLAGS = "Flags"

STANDARD_CASE_TOTAL_VALUE = "Total value:"

# Supporting documentation
SUPPORTING_DOCUMENTATION_TITLE = "Supporting documentation"
SUPPORTING_DOCUMENTATION_NAME = "Name"
SUPPORTING_DOCUMENTATION_DESCRIPTION = "Description"
SUPPORTING_DOCUMENTATION_DOCUMENT = "Document"
SUPPORTING_DOCUMENTATION_NO_DOCUMENTATION = "No supporting documentation"

COMBINE_USER_ADVICE = "Combine all user advice"
GIVE_OR_CHANGE_ADVICE = "Give or change advice"
CLEAR_ADVICE = "Clear advice"

DOCUMENT_TEMPLATES_TITLE = "Document templates"

REGISTER_BUSINESS_FIRST_AND_LAST_NAME = "First and last name"

USER_ADD_TITLE = "Add new user"
USER_EMAIL_QUESTION = "Whats the user's email"
USER_TEAM_QUESTION = "What team will the user belong to?"
USER_ROLE_QUESTION = "What role should this user have?"
USER_ADD_FORM_BACK_TO_USERS = "Back to users"
USER_EDIT_TITLE = "Edit user"
USER_EDIT_FORM_BACK_TO_USER = "Back to user"
USER_EDIT_FORM_SAVE = "Save"


class Common:
    SERVICE_NAME = "LITE Internal"


class Cases:
    BACK_TO_CASE = "Back to Case"
    GO_TO_QUEUE = "Go to queue"
    MANAGE_ORGANISATIONS = "Manage organisations"
    NO_CASES = "There are no new cases to show."
    EXPORTER_AMENDMENTS_BANNER = "See what cases have changed"
    ASSIGN_USERS = "Assign Users"
    STATUS = "Status"

    class Advice:
        ERROR = "There is a problem"
        IMPORT_ADVICE = "Import advice from picklists"
        IMPORT_PROVISO = "Import proviso from picklists"
        OTHER = "Is there anything else you want to say to the applicant? (optional)"
        REASON = "What are your reasons for this decision?"
        TEXT_ON_LICENCE = "This will appear on the generated documentation"

    class EcjuQueries:
        CASE_HAS_NO_QUERIES = "This case has no ECJU Queries"
        CLOSED = "Closed queries"
        OPEN = "Open queries"
        TITLE = "ECJU Queries"

        class AddQuery:
            ADD_BUTTON_LABEL = "Add an ECJU Query"
            DESCRIPTION = (
                "Enter a full description. If your question is related to goods, then include technical"
                " details if appropriate."
            )
            DROPDOWN_DESCRIPTION = (
                "You can:<ul><li>write a new question, or</li><li>choose a question from a list</li></ul>"
            )
            DROPDOWN_TITLE = "Ask a question"
            TITLE = "Write or edit your question"

    class Filters:
        SHOW_FILTERS = "Show filters"
        HIDE_FILTERS = "Hide filters"
        APPLY_FILTERS = "Apply filters"
        CLEAR_FILTERS = "Clear filters"
        FILTER_BY_CASE_TYPE = "Filter by case type"
        FILTER_BY_CASE_STATUS = "Filter by case status"

    class GenerateDocuments:
        BUTTON = "Generate A Document"
        TEMPLATES_TITLE = "Pick a Template"
        TITLE = "Generated Documents"

    class Manage:
        CASE_UPDATE_SUCCESSFUL = "Case updated successfully"

        class Documents:
            BUTTON = "Attached Documents"
            CASE_HAS_NO_DOCUMENTS = "This case has no documents"
            DESCRIPTION = "These are all the documents that have been uploaded to this case."
            DOWNLOAD_DOCUMENT = "Download document"
            PROCESSING = "Processing"
            TITLE = "Case Documents"
            VIRUS_INFECTED = "Virus infected"

            class AttachDocuments:
                BACK_TO_CASE_DOCUMENTS = "Back to Case Documents"
                BUTTON = "Attach Document"
                DESCRIPTION = "Maximum size: 100MB per file"
                DESCRIPTION_FIELD_DETAILS = "optional"
                DESCRIPTION_FIELD_TITLE = "Document description"
                FILE_TOO_LARGE = "The file you tried to upload was too large."
                TITLE = "Attach a document to this case"

        class MoveCase:
            BUTTON = "Move Case"
            DESCRIPTION = "Select all queues that apply."
            TITLE = "Where do you want to move this case?"

        class AssignUsers:
            DESCRIPTION = "Select all users that apply."
            MULTIPLE_TITLE = "Which users do you want to assign to these cases?"
            MULTIPLE_WARNING = "Users already assigned to these cases will be overwritten."
            TITLE = "Which users do you want to assign to this case?"

    class Case:
        BACK_TO_CASES_LINK = "Back to Cases"
        DESTINATION_HEADING = "Destinations"
        EDIT_CASE_FLAGS = "Edit case flags"
        EDIT_GOODS_FLAGS = "Edit goods flags"
        GOODS_HEADING = "Goods"
        GOODS_LOCATION_HEADING = "Goods location"
        REVIEW_GOODS = "Review Goods"

        class Tabs:
            class Activity:
                CHARACTER_LIMIT_2200 = "You can enter up to 2200 characters"
                MAKE_VISIBLE_TO_EXPORTER = "Make visible to exporter"

    class ReviewGoodsSummary:
        BACK_LINK = "Back to case"
        HEADING = "Review Goods"
        REVIEW_BUTTON = "Review and confirm item"
        SET_FLAGS = "Set goods flags"

    class ReviewGoodsForm:
        BACK_LINK = "Back to review goods"
        CONFIRM_BUTTON = "Add to Case"
        HEADING = "Check control list classification and add report summary"

    class RecordDecision:
        DENY = "Deny this application"
        GRANT = "Grant this application"
        TITLE = "Do you want to grant or deny this application?"


class RegisterBusiness:
    COMMERCIAL_OR_PRIVATE_INDIVIDUAL = "Commercial or private individual?"
    CREATE_ADMIN = "Create an admin for this organisation"
    CREATE_DEFAULT_SITE = "Create a default site for this exporter"
    CRN = "Company registration number (CRN)"
    CRN_DESCRIPTION = "8 numbers, or 2 letters followed by 6 numbers."
    DEFAULT_USER = "This will be the default user for this organisation."
    EMAIL = "Email"
    EORI_NUMBER = "European Union registration and identification number (EORI)"
    FIRST_NAME = "First name"
    GO_HOME = "Go home"
    GO_TO_COMPANIES = "Go to organisation list"
    LAST_NAME = "Last name"
    NAME = "What's the organisation's name?"
    NAME_OF_SITE = "Name of site"
    REGISTER_COMMERCIAL_TITLE = "Register an organisation"
    REGISTER_INDIVIDUAL_TITLE = "Register a private individual"
    REGISTRATION_COMPLETE = "Registration complete"
    SIC_NUMBER = "Classifies industries by a four-digit code."
    SUCCESSFULLY_REGISTERED = " Successfully registered"
    WHERE_IS_THE_EXPORTER_BASED = "Where is the exporter based?"

    class UkVatNumber:
        DESCRIPTION = (
            "9 digits long, with the first two letters indicating the country code of the registered business."
        )
        TITLE = "UK VAT number"


class Authentication:
    class UserDoesNotExist:
        DESCRIPTION = "You are not registered to use this system"
        TITLE = "User not found"


class Users:
    DESCRIPTION = "Team level users can manage and view team user accounts."
    INVITE = "Invite a new user"


class UpdateUser:
    class Status:
        DEACTIVATE_WARNING = "This user will no longer be able to log in or perform tasks"
        REACTIVATE_WARNING = "This user will be able to log in to and perform tasks"


class Activity:
    ADDED_AN_ECJU_QUERY = " added an ECJU query:"
    ADDED_A_CASE_NOTE = " added a case note:"


class Roles:
    DESCRIPTION = "Roles define permissions for users to perform a set of tasks"
    TITLE = "Roles"

    class Add:
        DESCRIPTION = ""
        TITLE = "Create a new role"

    class Edit:
        DESCRIPTION = ""
        TITLE = "Edit role"


class Queues:
    class QueueList:
        COLUMN_HEADING_ACTIONS = "Actions"
        COLUMN_HEADING_NAME = "Queue name"
        COLUMN_HEADING_TEAM = "Team name"
        PAGE_HEADING = "My work queues"

    class QueueAdd:
        PAGE_HEADING = "Add queue"
        QUESTION_TITLE = "Name"

    class QueueEdit:
        PAGE_HEADING = "Edit queue"
        QUESTION_TITLE = "Name"


class Flags:
    CREATE = "Create a flag"
    DESCRIPTION = "Flags are a simple way to tag cases, organisations, destinations and goods."
    TITLE = "Flags"

    class UpdateFlag:
        class Status:
            DEACTIVATE_HEADING = "Are you sure you want to deactivate this flag?"
            DEACTIVATE_WARNING = "This flag will no longer be able to be used unless it is reactivated"
            REACTIVATE_HEADING = "Are you sure you want to reactivate this flag?"
            REACTIVATE_WARNING = "This flag will be able to be used unless it is deactivated again"


class Picklist:
    TITLE = "Picklists"

    class Create:
        ECJU_QUERY = "Create an ECJU Query"
        FOOTNOTES = "Create a footnote"
        LETTER_PARAGRAPH = "Create a letter paragraph"
        PROVISO = "Create a proviso"
        REPORT_SUMMARY = "Create a report summary"
        STANDARD_ADVICE = "Create standard advice"

    class Edit:
        class Status:
            DEACTIVATE_HEADING = "Are you sure you want to deactivate this picklist item?"
            DEACTIVATE_WARNING = "This picklist item will no longer be able to be used unless it is reactivated"
            REACTIVATE_HEADING = "Are you sure you want to reactivate this picklist item?"
            REACTIVATE_WARNING = "This picklist item will be able to be used unless it is deactivated again"


class LetterTemplates:
    class AddParagraph:
        ADD_BUTTON = "Add items"
        HINT = "Select letter paragraphs to use in your template."
        TITLE = "Add letter paragraphs"

    class EditParagraph:
        ADD_LINK = "Add another letter paragraph"
        HINT = "Drag and drop letter paragraphs to reorder."
        REMOVE_BUTTON = "Remove letter paragraph from template"
        SAVE_BUTTON = "Save"
        TITLE = "Edit letter paragraphs"

    class OrderParagraph:
        ADD_PARAGRAPH = "Add a new paragraph"
        JS_HINT = "Drag and drop letter paragraphs to move them around"
        NO_JS_HINT = "Delete and add new paragraphs"
        PREVIEW_BUTTON = "Preview"
        REMOVE_BUTTON = "Remove letter paragraph from template"
        TITLE = "Choose the letter paragraphs you want to use in your letter"

    class Preview:
        SAVE_BUTTON = "Save"
        TITLE = "Preview"

    class LetterTemplates:
        CREATE_BUTTON = "Create a template"
        ERROR_BANNER = "An error occurred whilst processing your template"
        LAYOUT_COLUMN_TITLE = "Layout"
        NAME_COLUMN_TITLE = "Name"
        RESTRICTED_COLUMN_TITLE = "Restricted to"
        SUCCESSFULLY_CREATED_BANNER = "Your letter template was created successfully"
        TITLE = "Letter templates"
        UPDATED_COLUMN_TITLE = "Last updated"

    class LetterTemplate:
        BACK_LINK = "Back to letter templates"
        CREATED_TITLE = "Created at"
        EDIT_BUTTON = "Edit name and layout"
        EDIT_PARAGRAPH_BUTTON = "Add or edit paragraphs"
        LAST_UPDATE_TITLE = "Last updated"
        LAYOUT_TITLE = "Layout"
        RESTRICTED_TITLE = "Restricted to"

    class EditLetterTemplate:
        BUTTON_NAME = "Save"
        TITLE = "Edit %s"

        class Name:
            HINT = (
                "Call it something that:\n• Is easy to find\n• Explains when to use this template\n\n For example,"
                " 'Refuse a licence'."
            )
            TITLE = "Give your template a name"

        class CaseTypes:
            TITLE = "When should someone use this template?"

        class Layout:
            TITLE = "Choose a layout"

    class AddLetterTemplate:
        class Name:
            BACK_LINK = "Back to letter templates"
            CONTINUE_BUTTON = "Continue"
            HINT = (
                "Call it something that:\n• Is easy to find\n• Explains when to use this template\n\n For example,"
                " 'Refuse a licence'."
            )
            TITLE = "Give your template a name"

        class CaseTypes:
            CONTINUE_BUTTON = "Continue"
            TITLE = "When should someone use this template?"

        class Layout:
            CONTINUE_BUTTON = "Continue"
            TITLE = "Choose a layout"
