from django.urls import path
from . import views
from .views import (
    delete_segment,
    update_segment_texts,
    upload_video,
    merge_edited_audio_video,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("fpswd", views.fpswd, name="fpswd"),
    path("verify_otp", views.verify_otp, name="verify_otp"),
    path("set_pswd", views.set_pswd, name="set_pswd"),
    path("onboard/<int:pk>", views.onboard, name="onboard"),
    path("work_space/<int:pk>", views.work_space, name="work_space"),
    path("user_history/<int:pk>", views.user_history, name="user_history"),
    path(
        "delete-segment/<int:workspace_pk>/<int:segment_index>/",
        delete_segment,
        name="delete_segment",
    ),
    path(
        "update-segment-texts/<int:workspace_pk>/",
        update_segment_texts,
        name="update_segment_texts",
    ),
    path("upload_video/<int:pk>/", upload_video, name="upload_video"),
    path(
        "merge_edited_audio_video/<int:pk>/",
        merge_edited_audio_video,
        name="merge_edited_audio_video",
    ),
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin_side", views.admin_side, name="admin_side"),
    path("onboard/", views.onboard_login, name="onboard_login"),
    path("work_space/", views.workspace_login, name="workspace_login"),
    path("admin_logout", views.admin_logout, name="admin_logout"),
]
