# adapted from https://github.com/copier-org/copier-templates-extensions#context-hook-extension
from typing import Any

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    update = False

    def hook(self, context: dict[Any, Any]) -> dict[Any, Any]:
        context["uv_version"] = "0.5.9"
        context["pre_commit_version"] = "4.0.1"
        context["pyright_version"] = "1.1.390"
        context["pytest_version"] = "8.3.4"

        context["gha_checkout"] = "v4.2.2"
        context["gha_setup_python"] = "v5.3.0"
        context["gha_cache"] = "v4.2.0"
        context["gha_upload_artifact"] = "v4.4.3"
        context["gha_mutex"] = "d3d5b354d460d4b6a1e3ee5b7951678658327812 # v1.0.0-alpha.9"
        context["gha_linux_runner"] = "ubuntu-24.04"
        return context
