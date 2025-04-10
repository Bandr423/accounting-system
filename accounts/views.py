from django.contrib import messages

def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إنشاء الحساب بنجاح!")
            return redirect('list_accounts')
        else:
            messages.error(request, "حدث خطأ أثناء إنشاء الحساب.")
    else:
        form = AccountForm()
    return render(request, 'accounts/create_account.html', {'form': form})