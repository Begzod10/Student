from rest_framework import generics
from rest_framework.response import Response
from organizations.models.organization_landing_page import OrganizationLandingPage
from organizations.organization_landing_page.serializers.crud.crud import OrganizationLandingPageCrudSerializer


class OrganizationLandingPageDestroyApiView(generics.DestroyAPIView):
    queryset = OrganizationLandingPage.objects.all()
    serializer_class = OrganizationLandingPageCrudSerializer

    def delete(self, request, *args, **kwargs):
        obj_id = kwargs.get('pk')  # Assuming you're using the primary key in the URL
        try:
            instance = OrganizationLandingPage.objects.get(pk=obj_id)
            instance.deleted = True  # Call your overridden delete method
            return Response({"message": "Yo'nalish muvaffaqiyatli o'chirildi"},
                            status=200)  # Attach the status code here
        except OrganizationLandingPage.DoesNotExist:
            return Response({"error": "Object not found"}, status=404)
