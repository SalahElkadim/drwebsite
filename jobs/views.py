from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, JobApplication, CompanyRequest
from .forms import JobApplicationForm, CompanyRequestForm, JobForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone



# قائمة الوظائف
def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# تفاصيل وظيفة معينة
def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# نموذج التقديم على وظيفة
def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'jobs/application_success.html', {'job': job})
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_form.html', {'form': form, 'job': job})

# نموذج طلب وظيفة من شركة
def company_request(request):
    if request.method == 'POST':
        form = CompanyRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'jobs/request_success.html')
    else:
        form = CompanyRequestForm()
    return render(request, 'jobs/company_request.html', {'form': form})

@login_required
def company_applicants_view(request, company_request_id):
    company_request = get_object_or_404(CompanyRequest, id=company_request_id)
    job_applications = company_request.job_applications.all()  # لاحظ هنا التعديل
    
    context = {
        'company_request': company_request,
        'job_applications': job_applications,
    }
    return render(request, 'jobs/applicants_list.html', context)
    



# تحقق أن المستخدم هو صاحب الموقع (مثال: is_staff أو is_superuser)
def is_owner(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_owner)
def dashboard_home(request):
    jobs = Job.objects.all().order_by('-posted_at')
    applications = JobApplication.objects.all().order_by('-applied_at')[:5]
    company_requests = CompanyRequest.objects.all().order_by('-submitted_at')[:5]
    
    context = {
        'jobs': jobs,
        'applications': applications,
        'company_requests': company_requests,
    }
    return render(request, 'jobs/dashboard/home.html', context)

@login_required
@user_passes_test(is_owner)
def manage_jobs(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/dashboard/manage_jobs.html', {'jobs': jobs})

@login_required
@user_passes_test(is_owner)
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_jobs')
    else:
        form = JobForm()
    return render(request, 'jobs/dashboard/add_job.html', {'form': form})

@login_required
@user_passes_test(is_owner)
def toggle_job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.is_active = not job.is_active
    job.save()
    return redirect('manage_jobs')

@login_required
@user_passes_test(is_owner)
def view_applications(request):
    applications = JobApplication.objects.all().order_by('-applied_at')
    return render(request, 'jobs/dashboard/applications.html', {'applications': applications})

@login_required
@user_passes_test(is_owner)
def delete_application(request, job_id):
    apllication = get_object_or_404(JobApplication, id=job_id)
    apllication.delete()
    return redirect('view_applications')

@login_required
@user_passes_test(is_owner)
def view_company_requests(request):
    requests = CompanyRequest.objects.all().order_by('-submitted_at')
    return render(request, 'jobs/dashboard/company_requests.html', {'requests': requests})

@login_required
@user_passes_test(is_owner)
def show_company_request(request, request_id):
    company_request = get_object_or_404(CompanyRequest, id=request_id)
    return render(request, 'jobs/dashboard/show_company_request.html', {
        'company_request': company_request
    })

@login_required
@user_passes_test(is_owner)
def accept_company_request(request, request_id):
    company_request = get_object_or_404(CompanyRequest, id=request_id)
    company_request.status = 'accepted'
    company_request.accepted_at = timezone.now()
    company_request.save()
    messages.success(request, f'تم قبول طلب شركة {company_request.company_name} بنجاح')
    return redirect('show_company_request', request_id=request_id)

@login_required
@user_passes_test(is_owner)
def reject_company_request(request, request_id):
    company_request = get_object_or_404(CompanyRequest, id=request_id)
    company_request.status = 'rejected'
    company_request.save()
    messages.warning(request, f'تم رفض طلب شركة {company_request.company_name}')
    return redirect('show_company_request', request_id=request_id)

@login_required
@user_passes_test(is_owner)
def mark_contract_signed(request, request_id):
    company_request = get_object_or_404(CompanyRequest, id=request_id)
    company_request.contract_signed = True
    company_request.save()
    messages.success(request, f'تم تعيين العقد مع {company_request.company_name} كمكتمل')
    return redirect('show_company_request', request_id=request_id)


@login_required
@user_passes_test(is_owner)
def edit_job(request, job_id):
    # جلب الوظيفة من قاعدة البيانات أو عرض 404 إذا لم توجد
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        # إنشاء نموذج مع البيانات المرسلة وبيانات الوظيفة الحالية
        form = JobForm(request.POST, instance=job)
        
        if form.is_valid():
            # حفظ التعديلات إذا كان النموذج صالحاً
            form.save()
            
            # رسالة نجاح للمستخدم
            messages.success(request, 'تم تحديث الوظيفة بنجاح')
            
            # توجيه المستخدم إلى صفحة إدارة الوظائف
            return redirect('manage_jobs')
        else:
            # رسالة خطأ إذا كان النموذج غير صالح
            messages.error(request, 'حدث خطأ أثناء تحديث الوظيفة، يرجى مراجعة البيانات')
    else:
        # عرض النموذج مع بيانات الوظيفة الحالية
        form = JobForm(instance=job)
    
    # إعداد بيانات الصفحة
    context = {
        'job': job,
        'form': form,
    }
    
    # عرض صفحة التعديل
    return render(request, 'jobs/dashboard/edit_job.html', context)

@login_required
@user_passes_test(is_owner)
def accepted_companies(request):
    accepted_companies = CompanyRequest.objects.filter(
        status='accepted'
    ).order_by('-accepted_at')
    
    return render(request, 'jobs/dashboard/accepted_companies.html', {
        'accepted_companies': accepted_companies
    })

