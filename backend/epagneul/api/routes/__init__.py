from fastapi import APIRouter

#from .machines import router as machines_router
from .folders import router as folders_router

router = APIRouter()


router.include_router(folders_router, tags=["folders"], prefix="/folders")
#router.include_router(machines_router, tags=["machines"], prefix="/machines")
