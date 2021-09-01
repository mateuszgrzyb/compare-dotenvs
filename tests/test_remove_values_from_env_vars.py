import string

from faker import Faker

from compare_dotenvs import remove_values_from_env_vars


def test_remove_values_from_env_vars(faker: Faker):
    # given
    without_values = [
        faker.pystr_format(
            "?" * faker.random_int(1, 14), letters=string.ascii_uppercase + "_" * 5
        )
        + "="
        for _ in range(faker.random_int(0, 50))
    ]
    with_values = [f"{key}{faker.pystr()}" for key in without_values]

    # when
    with_removed_values = remove_values_from_env_vars(with_values)

    # then
    assert without_values == with_removed_values
