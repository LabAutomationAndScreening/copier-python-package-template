# adapted from https://github.com/copier-org/copier-templates-extensions#context-hook-extension
from typing import Any

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    update = False

    def hook(self, context: dict[Any, Any]) -> dict[Any, Any]:
        return context
