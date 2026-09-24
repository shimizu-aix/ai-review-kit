from core.models import Finding, Severity


def test_finding_to_json() -> None:
    f = Finding(
        rule_id="no-silent-except",
        severity=Severity.ERROR,
        file="app.py",
        line=42,
        message="例外が握り潰されています",
    )
    assert f.model_dump()["severity"] == "error"