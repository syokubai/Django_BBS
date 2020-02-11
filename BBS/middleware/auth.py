from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
import re


class LoginRequiredMiddleware(MiddlewareMixin):
    # ログイン必須にするためのミドルウェア
    def process_response(self, request, response):

        # django-allauthとメニュー画面のパスの場合、そのままページ遷移
        account_pattern = re.compile(r'^/bbs/accounts/*')
        menu_pattern = re.compile(r'^/bbs/menu/$')
        if account_pattern.match(request.path) or menu_pattern.match(request.path):
            return response

        # 上記以外のページに認証なしに遷移しようとするとログインページへ
        if not request.user.is_authenticated:
            messages.info(request, "ログインしてください")
            return HttpResponseRedirect('/bbs/accounts/login/')

        return response
