from .models import ProjectConfiguration

def project_contact_link_details(request):
    project_configuration_obj = ProjectConfiguration.objects.all().first()
    data = {
        'contact_email': project_configuration_obj.contact_email,
        'contact_phone': project_configuration_obj.contact_phone,
        'facebook_link': project_configuration_obj.facebook_link,
        'instagram_link': project_configuration_obj.instagram_link,
        'twitter_link': project_configuration_obj.twitter_link,
        'youtube_link': project_configuration_obj.youtube_link,
        'address': project_configuration_obj.address
    }
    return data