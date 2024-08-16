### Selenium

### Environment setup

Conda:

```bash
conda create --name scraper python=3.9
conda activate scraper
```

### Installation

Install Selenium:

```bash
python -m pip install selenium
```

### Run

```python
python scraper.py 
```

### TODO

如何解決iG安全性提示(有時會跳出提示告知是自動化登入，有安全性疑慮)

如何在自動瀏覽IG時，將所有圖片都隱藏，並置換圖框背景顏色。

製作一個腳本，不斷從搜尋裡透過關鍵字搜尋->點選進入user頁面->判斷是否點選Follow->下滑瀏覽post並下載圖片。(下載的圖片全部存在一個資料夾裡，如何判斷不重複儲存一樣的圖片？如何命名檔案？限制每個user下載圖片的數量？)

製作另一個腳本，不斷在Home頁面下滑瀏覽post，有時隨機點選post的like。



