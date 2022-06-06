from .abc import RegexSSHOutputVerifier


class LinuxSSHOutputVerifier(RegexSSHOutputVerifier):
    @property
    def cmd(self) -> str:
        return "uname -r"

    @property
    def regex(self) -> str:
        return r"\d+.\d+.\d+-[\w\d]+-[\w\d]+"
