@echo off
echo ==============================================
echo Installing required Python libraries...
echo ==============================================
python -m pip install -r requirements.txt

echo.
echo ==============================================
echo Step 1: Generating Initial supply chain Data...
echo ==============================================
python data_generator.py

echo.
echo ==============================================
echo Step 2: Training Supply Chain Risk ML Model...
echo ==============================================
python train_model.py

echo.
echo ==============================================
echo Step 3: Starting High-Performance Web Dashboard...
echo ==============================================
echo The app will automatically open in your default browser!
python app.py
pause
