import pandas as pd
import numpy as np

INPUT_FILE = 'amazon.csv' 
OUTPUT_FILE = 'clean_data_amazon.csv'

def clean_and_save_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print(f"Memuat data awal ({len(df)} baris)...")
        initial_length = len(df)
        
        # Ubah harga (Hapus '₹' dan konversi ke float)
        df['discounted_price'] = df['discounted_price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float, errors='ignore')
        df['actual_price'] = df['actual_price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float, errors='ignore')
        
        # Ubah persentase diskon (Hapus '%' --> konversi ke float, ubah error menjadi NaN)
        df['discount_percentage'] = pd.to_numeric(df['discount_percentage'].astype(str).str.replace('%', ''), errors='coerce')
        
        # Merapikan string (trim spasi & huruf kecil)
        for col in ['product_name', 'category', 'review_title', 'review_content']:
            if col in df.columns:
                 df[col] = df[col].astype(str).str.strip().str.lower()
        
        # Mengubah rating ke numerik. Semua string non-numeric (seperti error panjang) diubah ke NaN.
        if 'rating' in df.columns:
            df['rating'] = pd.to_numeric(df['rating'], errors='coerce') 

        # Hapus baris jika kolom kunci (ID) kosong
        df.dropna(subset=['product_id', 'review_id'], inplace=True)
        
        # Isi rating yang hilang dengan nilai rata-rata (Sekarang ini akan mencakup nilai 'NaN' yang baru dibuat)
        if 'rating' in df.columns:
            df['rating'].fillna(df['rating'].mean(), inplace=True)
            
        # Isi kolom teks yang kosong
        df['category'].fillna('unknown', inplace=True)
        df['review_content'].fillna('', inplace=True)

        # Penghapusan Duplikat
        df.drop_duplicates(subset=['product_id', 'user_id'], keep='first', inplace=True)

        # Pengurutan Data
        df.sort_values(by=['category', 'rating'], ascending=[True, False], inplace=True)
        
        # Simpan Data
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
        print(f"Baris awal: {initial_length}, Baris akhir: {len(df)}")
        
    except FileNotFoundError:
        print(f"ERROR!")
    except Exception as e:
        print(f"ERROR: Terjadi kesalahan saat memproses data: {e}")

if __name__ == "__main__":
    clean_and_save_data(INPUT_FILE)