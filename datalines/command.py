import io
import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class DatalinesCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional("data", required=True, otl_type=OTLType.TEXT),
            Keyword("sep", required=False, otl_type=OTLType.TEXT),
        ],
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        data = self.get_arg("data").value
        sep = self.get_arg("sep").value or ","

        self.log_progress("Converting to StringIO", stage=1, total_stages=2)
        file_like = io.StringIO(data)

        self.log_progress("Preparing the DataFrame", stage=2, total_stages=2)
        df = pd.read_csv(file_like, sep=sep)

        return df
