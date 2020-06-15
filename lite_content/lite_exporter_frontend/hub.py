TITLE = "Exporter hub"
ACCOUNT = "Export control account"


class Header:
    ACCOUNT_HOME = "Account home"
    SWITCH_ORG = "Switch organisation"


class Navigation:
    ACCOUNT_HOME = "Account home"
    YOUR_ACCOUNT = "Manage your organisation and personal details"


class Tiles:
    APPLY_FOR_LICENCE = "Apply"
    APPLICATIONS = "Check progress"
    VIEW_AND_MANAGE_LICENCES = "Licences and clearances"
    GOODS = "Product list"
    END_USER_ADVISORIES = "End user advisories"
    OPEN_LICENCE_RETURNS = "Open licence returns"
    COMPLIANCE_HEADING = "Compliance and annual returns"

    # Standard dashboard
    class Apply:
        APPLY_FOR = "Apply for:"
        EXPORT_LICENCES = "export licences"
        TRADE_CONTROL_LICENCES = "trade control licences"
        TRANSHIPMENT_LICENCES = "transhipment licences"
        MOD_CLEARANCES = "MOD clearances"
        REGISTER_OGEL = "Register for open general licences (OGLs)."

    class Applications:
        CHECK_PROGRESS = "View the status of submitted applications and registrations."
        EDIT_APPLICATIONS = "Edit, withdraw or copy applications."

    class Licences:
        DESCRIPTION = "View and manage your licences and clearances, including NLRs and unsuccessful applications."

    class ProductList:
        MANAGE_PRODUCTS = "View and manage your organisation's product database."
        PRODUCTS_INCLUDE = "Products include goods, items, technology, data and services."
        CLC_LINK = "Create a control list classification (CLC) query"
        GRADING_LINK = "Apply for a security grading"

    class EUA:
        ASK_FOR_ADVICE = (
            "Ask for advice about an overseas organisation, government or individual in your export of products "
            "that are not controlled."
        )

    # HMRC Dashboard
    class CustomsEnquiry:
        MAKE_ENQUIRY = "Make a customs enquiry"
        DRAFT_LINK = "Draft applications"

    class CheckProgress:
        TITLE = "Check progress"
        VIEW_STATUS = "View the status of your enquiries."

    # Compliance
    class OpenLicenceReturns:
        DESCRIPTION = "View and manage your open licence returns"
        ADD_LINK = "Submit"
        VIEW_LINK = "View licence returns"
