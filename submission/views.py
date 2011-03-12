from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .models import Submission
from .forms import SubmissionForm

def submission(request):
    if request.method == 'POST':
        submission_form = SubmissionForm(request.POST)

        if submission_form.is_valid():
            submission = submission_form.save()

            return HttpResponseRedirect('/submission/thankyou')
    else:
        submission_form = SubmissionForm()

    return render_to_response("submission/submission.html", {
        'submission_form': submission_form,
    }, context_instance=RequestContext(request))


