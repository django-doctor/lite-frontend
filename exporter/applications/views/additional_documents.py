from django.shortcuts import render
from django.views.generic import TemplateView

from exporter.applications.services import get_additional_documents

from core.auth.views import LoginRequiredMixin


class AdditionalDocuments(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        application_id = str(kwargs["pk"])
        data, _ = get_additional_documents(request, application_id)

        context = {
            "additional_documents": data["documents"],
            "application_id": application_id,
            "editable": data["editable"],
        }

        return render(request, "applications/additional-documents/additional-documents.html", context)
