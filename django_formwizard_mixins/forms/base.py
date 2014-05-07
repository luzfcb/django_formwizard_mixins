from django import forms

class BaseConfirmationForm(forms.Form):
    @property
    def ordered_form_map(self):
        if self._ordered_form_map is None:
            raise AttributeError("You cannot reference 'ordered_form_map' before calling the 'set_forms' method!")
        return self._ordered_form_map
    _ordered_form_map = None
    
    def set_forms(self, ordered_form_map):
        self._ordered_form_map = ordered_form_map


class AllPreviousFormsConfirmationForm(BaseConfirmationForm):
    def set_forms(self, ordered_form_map):
        super(AllPreviousFormsConfirmationForm, self).set_forms(ordered_form_map)

        for form in self.ordered_form_map.values():
            if hasattr(form, "cleaned_data"):
                if not isinstance(form, BaseConfirmationForm):
                    for field_name in form.cleaned_data:
                        field = form.fields[field_name]
                        # label_template = '\n%s: <input type="text" value="%s" readonly="true" disabled="true" />'
                        label_template = '\n%s - %s'
                        if field.label:
                            label = label_template % (field.label, form.cleaned_data[field_name])
                        else:
                            label = label_template % (field_name, form.cleaned_data[field_name])
                        self.fields["%sconfirm" % field_name] = forms.BooleanField(label=label)