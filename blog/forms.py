from django import forms
from django.forms import ModelForm
from blog.models import BlogEntry, Category
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, HTML, Div


class BlogEntryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogEntryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.render_unmentioned_fields = False

        self.helper.layout = Layout(
            Div(
                Row(
                    Column(Field('category', v_model='category'), css_class='col-lg-5 form-center')
                ),
                Row(
                    Column(Field('title', v_model='title'), css_class='col-lg-5 form-center')
                ),
                Row(
                    Column(Field('text_entry', v_model='text_entry', rows='17'),
                           css_class='col-lg-5 form-center')
                ),
                Row(
                    Column(
                        Div(
                            Div(
                                Div(
                                    Field('private', v_model='private'),
                                    css_class='custom-control custom-checkbox mr-sm-2',
                                    style='display: inline-block'
                                ),
                                HTML(
                                    """
                                        <button type="submit" class="btn btn-outline-blue&#45;&#45;dark btn-wide">
                                            Save Changes
                                        </button> 
                                    """
                                ),
                            ) if self.is_valid() else
                            HTML("""
                                <div class="btn-group">
                                  <button type="submit" class="btn btn-outline-blue--dark btn-wide" @click="submitForm(null)">Post</button>
                    
                                  <button type="button" class="btn btn-outline-blue--dark btn-dropdown btn-dropdown-short"
                                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <span class="sr-only">Toggle Post Options Dropdown</span>
                                    <i class="fas fa-sort-down"></i>
                                  </button>
                    
                                  <div class="dropdown-menu">
                                    <a type="button" class="btn dropdown-item" onClick='submitPrivatePost()'>Post Privately</a>
                                  </div>
                                </div>
                              </div>
                            """),
                            css_class='text-right'
                        ),
                        css_class='col-lg-5 form-center'
                    )
                ),
                css_class='text-lg-form-wrapper',

            ),
        )

    class Meta:
        model = BlogEntry
        fields = [
            'category',
            'text_entry',
            'private',
            'title'
        ]

    def save(self, commit=True):
        blog_instance = super(BlogEntryForm, self).save(commit=False)
        blog_instance.date_of_submission = datetime.now()
        blog_instance.date_updated = datetime.now()

        return blog_instance
