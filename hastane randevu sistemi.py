#210101052 Tarık Yalçın
#210101058 Cemre Hasırcı


import tkinter as tk
from tkinter import messagebox, ttk

class Randevu:
    def __init__(self, poliklinik, doktor, tarih, saat):
        self.poliklinik = poliklinik
        self.doktor = doktor
        self.tarih = tarih
        self.saat = saat
        self.next = None

class Kullanici:
    def __init__(self, isim, sifre):
        self.isim = isim
        self.sifre = sifre
        self.randevular = None  #boş linked list halihazırda alınmış bir randevu bulunmadığı için

# Kullanıcı bilgilerini tuutuğumuz kısım
kullanici_bilgileri = {
    '1' : Kullanici('Ayşe', '1'),
    '12345678901': Kullanici('Ahmet', 'ahmet123'),
    
}

# Poliklinik ve doktor bilgileri
poliklinikler = {
    'Kardiyoloji': ['Dr. Ahmet', 'Dr. Mehmet', 'Dr. Ayşe', 'Dr. Fatma'],
    'Dermatoloji': ['Dr. Ali', 'Dr. Hasan', 'Dr. Hüseyin', 'Dr. Can'],
    'Nöroloji': ['Dr. İsmail', 'Dr. Deniz', 'Dr. Mehmet', 'Dr. Bilge'],
    'Ortopedi': ['Dr. Sezer', 'Dr. Hasan', 'Dr. Göksel', 'Dr. Can'],
    'Göz Hastalıkları': ['Dr. İsmail', 'Dr. Rüzgar', 'Dr. Mehmet', 'Dr. Ayşe'],
    'KBB': ['Dr. Kayra', 'Dr. Hasan', 'Dr. Burcu', 'Dr. Can'],
    'Dahiliye': ['Dr. İsmail', 'Dr. Ahmet', 'Dr. Koray', 'Dr. Ayşe'],
    'Çocuk Sağlığı ve Hastalıkları': ['Dr. Yiğit', 'Dr. Kemal', 'Dr. Duru', 'Dr. Fatma'],
    'Kadın Hastalıkları ve Doğum': ['Dr. İsmail', 'Dr. Doğa', 'Dr. Mehmet', 'Dr. Ayşe'],
    'Psikiyatri': ['Dr. Ali', 'Dr. Hasan', 'Dr. Hüseyin', 'Dr. Pelin']
}

def giris_yap():
    global kullanici
    tc = tc_entry.get()
    sifre = sifre_entry.get()
    if tc in kullanici_bilgileri and kullanici_bilgileri[tc].sifre == sifre:
        kullanici = kullanici_bilgileri[tc]  
        giris_ekrani.pack_forget()
        hosgeldin_label.config(text=f"Hoşgeldiniz {kullanici.isim}")
        ana_ekran.pack()
    else:
        messagebox.showerror("Giriş Başarısız", "TC Kimlik Numarası veya Şifre yanlış")

def kayit_ol():
    kayit_ekrani = tk.Toplevel(root)
    kayit_ekrani.geometry("300x300")
    kayit_ekrani.title("Kayıt Ol")
    kayit_ekrani.geometry("+{}+{}".format(650,250))

    tk.Label(kayit_ekrani, text="TC Kimlik No:").pack(pady=10)
    yeni_tc_entry = tk.Entry(kayit_ekrani)
    yeni_tc_entry.pack(pady=10)

    tk.Label(kayit_ekrani, text="Şifre:").pack(pady=10)
    yeni_sifre_entry = tk.Entry(kayit_ekrani, show="*")
    yeni_sifre_entry.pack(pady=10)

    tk.Label(kayit_ekrani, text="İsim:").pack(pady=10)
    yeni_isim_entry = tk.Entry(kayit_ekrani)
    yeni_isim_entry.pack(pady=10)

    tk.Button(kayit_ekrani, text="Kayıt Ol", command=lambda: kayit_onayla(yeni_tc_entry.get(), yeni_sifre_entry.get(), yeni_isim_entry.get(), kayit_ekrani)).pack(pady=10)

def kayit_onayla(tc, sifre, isim, kayit_ekrani):
    if tc not in kullanici_bilgileri:
        kullanici_bilgileri[tc] = Kullanici(isim, sifre)
        messagebox.showinfo("Kayıt Başarılı", "Kayıt işlemi başarıyla tamamlandı.")
        kayit_ekrani.destroy()
    else:
        messagebox.showerror("Hata", "Bu TC Kimlik Numarası zaten kayıtlı.")

def randevu_al():
    ana_ekran.pack_forget()
    poliklinik_secim_ekrani.pack()
    poliklinik_secim.set(' ')  # Poliklinik seçimini sıfırla
    doktor_secim.set('Doktor:')  # Doktor seçimini sıfırla

def poliklinik_sec():
    secilen_poliklinik = poliklinik_secim.get()
    if secilen_poliklinik != ' ':  # Kullanıcının bir seçim yaptığından emin ol
        poliklinik_secim_ekrani.pack_forget()
        doktor_secim['values'] = sorted(poliklinikler[secilen_poliklinik])  # Doktorları gsöter
        doktor_secim_ekrani.pack()
    else:
        messagebox.showerror("Hata", "Lütfen bir poliklinik seçin")

def doktor_sec():
    secilen_doktor = doktor_secim.get()
    if secilen_doktor != 'Doktor:':  # Kullanıcının bir seçim yaptığından emin ol
        doktor_secim_ekrani.pack_forget()
        tarih_secim.set('Tarih:')  # Tarih seçimini sıfırla
        saat_secim.set('Saat:')  # Saat seçimini sıfırla
        tarih_secim_ekrani.pack()
    else:
        messagebox.showerror("Hata", "Lütfen bir doktor seçin")

def randevu_onayla():
    secilen_tarih = tarih_secim.get()
    secilen_saat = saat_secim.get()
    poliklinik = poliklinik_secim.get()
    doktor = doktor_secim.get()

    if secilen_tarih != 'Tarih:' and secilen_saat != 'Saat:':
        if not is_randevu_available(poliklinik, doktor, secilen_tarih, secilen_saat):
            messagebox.showerror("Hata", "Seçilen saatte randevu alınamaz. Lütfen başka bir saat seçin.")
        else:
            tarih_secim_ekrani.pack_forget()
            eklenen_randevu(poliklinik, doktor, secilen_tarih, secilen_saat)
            messagebox.showinfo("Randevu Onaylandı", f"Randevunuz onaylandı!\nPoliklinik: {poliklinik}\nDoktor: {doktor}\nTarih: {secilen_tarih}\nSaat: {secilen_saat}")
            ana_ekran.pack()
    else:
        messagebox.showerror("Hata", "Lütfen bir tarih ve saat seçin")

def is_randevu_available(poliklinik, doktor, tarih, saat):
    current = kullanici.randevular
    while current is not None:
        if (
            current.poliklinik == poliklinik
            and current.doktor == doktor
            and current.tarih == tarih
            and current.saat == saat
        ):
            return False
        current = current.next
    return True

def randevularim():
    ana_ekran.pack_forget()
    randevular_ekrani.pack()
    if kullanici.randevular:  # Eer kullanıcının randevuları varsa
        current = kullanici.randevular
        i = 1
        while current is not None:
            tk.Label(randevular_ekrani, text=f"Randevu {i}:\nPoliklinik: {current.poliklinik}\nDoktor: {current.doktor}\nTarih: {current.tarih}\nSaat: {current.saat}").pack(pady=10)
            tk.Button(randevular_ekrani, text="Randevuyu Sil", command=lambda current=current: randevu_sil(current)).pack(pady=10)
            current = current.next
            i += 1
    else:  # Kullanıcının randevuları yoksa
        tk.Label(randevular_ekrani, text="Randevunuz Bulunmamaktadır").pack(pady=10)
    tk.Button(randevular_ekrani, text="Geri", command=geri).pack(pady=10)

def eklenen_randevu(poliklinik, doktor, tarih, saat):
    new_randevu = Randevu(poliklinik, doktor, tarih, saat)
    new_randevu.next = kullanici.randevular
    kullanici.randevular = new_randevu

def randevu_sil(randevu):
    current = kullanici.randevular
    if current == randevu:
        kullanici.randevular = current.next
    else:
        while current.next != randevu:
            current = current.next
        current.next = current.next.next
    geri()  # Randevu ekranını yenile

def geri():
    randevular_ekrani.pack_forget()
    for widget in randevular_ekrani.winfo_children():
        widget.destroy()  # Randevu ekranını temizle
    ana_ekran.pack()

root = tk.Tk()
root.geometry("400x400")
root.title("Hastane Randevu Sistemi")
# Pencerenin ekrandaki konumu
root.geometry("+{}+{}".format(600,200))

giris_ekrani = tk.Frame(root)
tk.Label(giris_ekrani, text="TC Kimlik No:").pack(pady=10)
tc_entry = tk.Entry(giris_ekrani)
tc_entry.pack(pady=10)

tk.Label(giris_ekrani, text="Şifre:").pack(pady=10)
sifre_entry = tk.Entry(giris_ekrani, show="*")
sifre_entry.pack(pady=10)

tk.Button(giris_ekrani, text="Giriş Yap", command=giris_yap).pack(side="left", padx=10, pady=10)
tk.Button(giris_ekrani, text="Kayıt Ol", command=kayit_ol).pack(side="left", padx=10, pady=10)

giris_ekrani.pack()

ana_ekran = tk.Frame(root)
hosgeldin_label = tk.Label(ana_ekran)
hosgeldin_label.pack(pady=10)
tk.Button(ana_ekran, text="Randevu Al", command=randevu_al).pack(pady=10)
tk.Button(ana_ekran, text="Randevularım", command=randevularim).pack(pady=10)

poliklinik_secim_ekrani = tk.Frame(root)
poliklinik_secim = tk.StringVar(value=None)
for poliklinik in poliklinikler.keys():
    tk.Radiobutton(poliklinik_secim_ekrani, text=poliklinik, variable=poliklinik_secim, value=poliklinik).pack(anchor='w')
tk.Button(poliklinik_secim_ekrani, text="Onayla", command=poliklinik_sec).pack(pady=10)

doktor_secim_ekrani = tk.Frame(root)
doktor_secim = ttk.Combobox(doktor_secim_ekrani, state="readonly")
doktor_secim.pack(pady=10)

tk.Button(doktor_secim_ekrani, text="Onayla", command=doktor_sec).pack(pady=10)

tarih_secim_ekrani = tk.Frame(root)
tarih_secim = ttk.Combobox(tarih_secim_ekrani, values=[f"{i}-12-23" for i in range(1, 6)], state="readonly")
tarih_secim.set("Tarih:")
tarih_secim.pack(pady=10)

saat_secim = ttk.Combobox(tarih_secim_ekrani, values=[f"{i}:00" for i in range(8, 17)], state="readonly")
saat_secim.set("Saat:")
saat_secim.pack(pady=10)
tk.Button(tarih_secim_ekrani, text="Randevu Al", command=randevu_onayla).pack(pady=10)

randevular_ekrani = tk.Frame(root)

root.mainloop()
