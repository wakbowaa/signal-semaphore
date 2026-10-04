from pathlib import Path
SOURCE=(Path(__file__).parents[1]/"contracts"/"contract.py").read_text(encoding="utf-8")
def test_surface():
    for name in ["open_game","transmit","answer","get_game","get_games_page","get_summary"]: assert f"def {name}" in SOURCE
def test_consensus_and_guards():
    for term in ["run_nondet_unsafe","different wallet","forbidden","LINE_CLEAR","LINE_BLOCKED"]: assert term in SOURCE
def test_runner(): assert SOURCE.startswith('# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }')
