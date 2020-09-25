from django.urls import path

from .views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    PaymentView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    add_single_item_to_cart,
    AddCouponView,
    RequestRefundView,

    # account
    login_request,
    logout_request,
    signup_request,
    changepass

)

urlpatterns = [
    # Account
    path('accounts/login/', login_request, name="login"),
    path('accounts/logout/', logout_request, name="logout"),
    path('signup/', signup_request, name="signup"),
    path('accounts/changepass/', changepass, name="changepass"),

    # Ecom

    path('', HomeView.as_view(), name='home'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add_single_item_to_cart/<slug>/', add_single_item_to_cart, name='add_single_item_to_cart'),
    path('remove_single_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]
