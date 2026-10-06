from courseProjectCode.Metrics import maintainability, testability


def test_collection_hook_counts_collected_items():
    plugin = testability.TestCounterPlugin()

    plugin.pytest_collection_modifyitems([object(), object(), object()])

    assert plugin.test_count == 3


def test_testability_main_uses_stubbed_runner_and_coverage(monkeypatch, capsys):
    events = []

    class StubCoverage:
        def __init__(self, source):
            events.append(("coverage_init", source))

        def start(self):
            events.append(("coverage_start",))

        def stop(self):
            events.append(("coverage_stop",))

        def save(self):
            events.append(("coverage_save",))

        def report(self):
            events.append(("coverage_report",))

    def stub_pytest_main(args, plugins):
        events.append(("pytest_main", args))
        plugins[0].pytest_collection_modifyitems([object(), object()])

    monkeypatch.setattr(testability.coverage, "Coverage", StubCoverage)
    monkeypatch.setattr(testability.pytest, "main", stub_pytest_main)

    testability.main()

    assert events == [
        ("coverage_init", ["pandas/core"]),
        ("coverage_start",),
        ("pytest_main", ["pandas/tests"]),
        ("coverage_stop",),
        ("coverage_save",),
        ("coverage_report",),
    ]
    assert "Total test cases found: 2" in capsys.readouterr().out


def test_maintainability_main_aggregates_source_analysis(monkeypatch, capsys):
    class StubAnalysis:
        def __init__(self, code_count, documentation_count):
            self.code_count = code_count
            self.documentation_count = documentation_count

    analyses = {
        "pandas/core/first.py": StubAnalysis(3, 1),
        "pandas/core/second.py": StubAnalysis(2, 2),
    }

    def stub_from_file(file_path, group):
        assert group == "core"
        if file_path == "pandas/core/broken.py":
            raise OSError("unreadable source")
        return analyses[file_path]

    monkeypatch.setattr(
        maintainability.os,
        "walk",
        lambda _root: [("pandas/core", [], ["first.py", "second.py", "broken.py"])],
    )
    monkeypatch.setattr(
        maintainability.SourceAnalysis, "from_file", stub_from_file
    )

    maintainability.main()

    output = capsys.readouterr().out
    assert "pandas/core/first.py\t\t3\t\t25%" in output
    assert "pandas/core/second.py\t\t2\t\t50%" in output
    assert "Total\t\t\t8\t\t37%" in output
    assert "broken.py" not in output