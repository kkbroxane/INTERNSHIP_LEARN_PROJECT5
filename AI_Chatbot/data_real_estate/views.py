# from django import forms
# from django.shortcuts import redirect
# from django.urls import reverse
# from formtools.wizard.views import SessionWizardView
# from .forms import BasePropertyForm, LogementForm, ProfessionelForm
# from .models import Logement, Professionel, Terrain

# FORMS = [
#     ("base", BasePropertyForm),
#     ("logement", LogementForm),
#     ("professionel", ProfessionelForm),
# ]

# TEMPLATES = {
#     "base": "form/property_form.html",
#     "logement": "form/property_form.html",
#     "professionel": "form/property_form.html",
# }

# class PropertyWizard(SessionWizardView):
#     form_list = FORMS
#     template_name = "form/property_form.html"

#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]

#     def get_form_list(self):
#         form_list = super().get_form_list()

#         for form_class in form_list.values():
#             for name, field in form_class.base_fields.items():
#                 field.is_boolean = isinstance(field, forms.BooleanField)

#         step_data = self.storage.get_step_data('base')
#         if not step_data:
#             return form_list

#         property_type = step_data.get('base-property_type')
#         if not property_type:
#             return form_list

#         if property_type in ['villa', 'maison', 'appartement']:
#             form_list.pop('professionel', None)

#         elif property_type in ['bureau', 'boutique']:
#             form_list.pop('logement', None)

#         else:
#             form_list.pop('logement', None)
#             form_list.pop('professionel', None)

#         return form_list

#     def done(self, form_list, **kwargs):
#         data = self.get_all_cleaned_data()

#         property_type = data['property_type']

#         if property_type in ['villa', 'maison', 'appartement']:
#             logement = Logement.objects.create(
#                 transaction_type=data['transaction_type'],
#                 property_type=property_type,
#                 location=data['location'],
#                 surface_area=data['surface_area'],
#                 price=data['price'],
#                 nb_bedrooms=data['nb_bedrooms'],
#                 nb_bathrooms=data['nb_bathrooms'],
#                 has_parking=data['has_parking'],
#                 is_furnished=data['is_furnished']
#             )
#             logement.generate_embedding_for_property()
#             return redirect(reverse('property_detail', kwargs={'p_id': logement.id}))

#         elif property_type in ['bureau', 'boutique']:
#             professionel = Professionel.objects.create(
#                 transaction_type=data['transaction_type'],
#                 property_type=property_type,
#                 location=data['location'],
#                 surface_area=data['surface_area'],
#                 price=data['price'],
#                 nb_rooms=data['nb_rooms'],
#                 nb_bathrooms=data['nb_bathrooms'],
#                 is_furnished=data['is_furnished']
#             )
#             professionel.generate_embedding_for_property()
#             return redirect(reverse('property_detail', kwargs={'p_id': professionel.id}))

#         else:
#             terrain = Terrain.objects.create(
#                 transaction_type=data['transaction_type'],
#                 property_type=property_type,
#                 location=data['location'],
#                 surface_area=data['surface_area'],
#                 price=data['price']
#             )
#             terrain.generate_embedding_for_property()
#             return redirect(reverse('property_detail', kwargs={'p_id': terrain.id}))
