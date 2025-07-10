


from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


# Mô hình phân trang
class Pagination(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int


# Response chuẩn hỗ trợ phân trang
class ResponseSchema(BaseModel, Generic[T]):
    status: str
    message: str
    data: Optional[T] = None
    pagination: Optional[Pagination] = None


def success_response(
    data, message: str = "Success", pagination: Optional[Pagination] = None
):
    return ResponseSchema(
        status="success",
        message=message,
        data=data,
        pagination=pagination,
    )


def success_response_with_pagination(
    data, message: str = "Success", pagination: Optional[Pagination] = None
):
    return ResponseSchema(
        status="success",
        message=message,
        data=data,
        pagination=pagination,
    )
