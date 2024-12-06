"""
 Copyright (c) 2024 Yihuai Gao
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

def steady_clock_us() -> int: ...
def system_clock_us() -> int: ...

class RMQServer:
    def __init__(self, server_name: str, server_endpoint: str) -> None: ...
    def add_topic(self, topic: str, max_remaining_time: float) -> None: ...
    def put_data(self, topic: str, data: bytes) -> None: ...
    def peek_data(
        self, topic: str, end_type: str, n: int
    ) -> tuple[list[bytes], list[float]]: ...
    def pop_data(
        self, topic: str, end_type: str, n: int
    ) -> tuple[list[bytes], list[float]]: ...
    def get_topic_status(self) -> dict[str, int]: ...
    def get_timestamp(self) -> float: ...
    def reset_start_time(self, system_time_us: int) -> None: ...
    def wait_for_request(self, topic: str, timeout: float) -> tuple[list[bytes], list[float]]: ...
    def reply_request(self, topic: str, data: list[bytes]) -> None: ...

class RMQClient:
    def __init__(self, client_name: str, server_endpoint: str) -> None: ...
    def peek_data(
        self, topic: str, end_type: str, n: int
    ) -> tuple[list[bytes], list[float]]: ...
    def pop_data(
        self, topic: str, end_type: str, n: int
    ) -> tuple[list[bytes], list[float]]: ...
    def get_last_retrieved_data(self) -> tuple[list[bytes], list[float]]: ...
    def get_timestamp(self) -> float: ...
    def reset_start_time(self, system_time_us: int) -> None: ...
    def request_with_data(self, topic: str, data: list[bytes]) -> tuple[list[bytes], list[float]]: ...
