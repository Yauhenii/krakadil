from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["config/settings.yaml", "config/.secrets.yaml"],
    environments=True,
)
