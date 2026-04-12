from pathlib import Path


def list_text_files(data_dir: Path) -> list[Path]:
	"""Return sorted .txt files from the given data directory."""
	return sorted(data_dir.glob("*.txt"))


def main() -> None:
	data_dir = Path("data/text_files")
	files = list_text_files(data_dir)

	if not files:
		print("No text files found in data/text_files")
		return

	print(f"Found {len(files)} text file(s):")
	for file_path in files:
		preview = file_path.read_text(encoding="utf-8").splitlines()[0]
		print(f"- {file_path.name}: {preview}")


if __name__ == "__main__":
	main()
