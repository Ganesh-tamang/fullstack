import time
import logging
from django.utils.deprecation import MiddlewareMixin

from user.models import RequestLog
class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        try:
            duration = (time.time() - request._start_time) * 1000  # ms
            method = request.method
            path = request.get_full_path()

            # Save to DB
            RequestLog.objects.create(
                method=method,
                path=path,
                duration_ms=duration,
            )
        except Exception:
            pass
        return response