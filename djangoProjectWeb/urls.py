"""
URL configuration for djangoProjectWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import Loginform, MyPasswordResetForm, MypasswordChangeForm, MysetPasswordForm

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='site-home'),
                  path('about-us/', views.about, name='about-us'),
                  path('contact-us/', views.contact, name='contact-us'),
                  path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
                  path('category/title/<val>', views.CategoryTitle.as_view(), name='category-title'),
                  path('product-detail/<int:pk>', views.ProductDetail.as_view(), name='product-detail'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('address/', views.address, name='address'),
                  path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAdress'),
                  # It expects a pk (primary key) as a parameter in the URL, which is used to identify the specific
                  # customer whose address is being updated.

                  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
                  path('cart/', views.show_cart, name='showcart'),
                  path('checkout/', views.checkout.as_view(), name='checkout'),
                  path('search/', views.search, name='search'),

                  path('plus-cart/', views.plus_cart),
                  path('minus-cart/', views.minus_cart),
                  path('remove-cart/', views.plus_cart),
                  path('pluswishlsit/', views.plus_wishlist),
                  path('minuswishlist/', views.minus_wishlist),
                  path('wishlist/', views.show_wishlist, name='wishlist'),

                  # loginregistration

                  path('registration/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
                  path('login/',
                       auth_view.LoginView.as_view(template_name='loginform.html', authentication_form=Loginform),
                       name='login'),
                  path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html',
                                                                               form_class=MypasswordChangeForm,
                                                                               success_url='/passwordchangedone'),
                       name='password-change'),
                  path('passwordchangedone/',
                       auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),
                       name='passwordchangedone'),

                  path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

                  path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',
                                                                              form_class=MyPasswordResetForm,
                                                                              ), name='password_reset'),
                  path('password-reset/done/',
                       auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                       name='password_reset_done'),
                  path('password-reset-confirm/<uidb64>/<token>/',
                       auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                                  form_class=MysetPasswordForm),
                       name='password_reset_confirm'),
                  path('password-reset-complete/',
                       auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                       name='password_reset_complete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Tony enterprises"
admin.site.site_title = "Tony enterprises"
admin.site.site_index_title = "Welcome to Tony enterprises"
