# ================================================================
# Paths
# ================================================================
PRIVATE_RAW = data/raw/private_schools.geojson
PUBLIC_RAW  = data/raw/public_schools.geojson
OUTPUT      = data/processed/sf_schools.geojson
SCRIPT      = scripts/clean_schools.py

# Default target when running just `make`
all: schools

# ================================================================
# Ensure necessary directories exist
# ================================================================
setup:
	mkdir -p data/raw
	mkdir -p data/processed
	@echo "✔ Directory structure ready."

# ================================================================
# Build cleaned school dataset
# ================================================================
schools: $(SCRIPT) $(PRIVATE_RAW) $(PUBLIC_RAW) | setup
	python3 $(SCRIPT) $(PRIVATE_RAW) $(PUBLIC_RAW) $(OUTPUT)
	@echo "✔ Created: $(OUTPUT)"

# ================================================================
# Clean processed outputs
# ================================================================
clean:
	rm -f data/processed/*.geojson
	@echo "✔ Cleaned processed datasets"
