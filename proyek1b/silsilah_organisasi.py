"""Silsilah Organisasi UIN Suska Riau (prototype) - General Tree.
Jalankan: python silsilah_organisasi.py"""


class Node:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.bawahan = []                       # daftar anak (general tree)

    def __str__(self):
        return f"{self.nama} ({self.jabatan})"


class TreeOrganisasi:
    def __init__(self, root):
        self.root = root

    def insert_node(self, nama_atasan, nama, jabatan):
        """Sisipkan pegawai baru di bawah atasan tertentu."""
        for node in self.preorder():
            if node.nama == nama_atasan:
                node.bawahan.append(Node(nama, jabatan))
                return True
        return False                            # atasan tidak ditemukan

    def search_node(self, kata):
        """Cari pegawai berdasarkan nama atau jabatan."""
        kata = kata.lower()
        return [n for n in self.preorder()
                if kata in n.nama.lower() or kata in n.jabatan.lower()]

    def preorder(self):
        """Node -> anak-anak."""
        hasil = []
        def kunjungi(node):
            hasil.append(node)
            for anak in node.bawahan:
                kunjungi(anak)
        kunjungi(self.root)
        return hasil

    def inorder(self):
        """Anak pertama -> Node -> anak-anak sisanya."""
        hasil = []
        def kunjungi(node):
            if node.bawahan:
                kunjungi(node.bawahan[0])
            hasil.append(node)
            for anak in node.bawahan[1:]:
                kunjungi(anak)
        kunjungi(self.root)
        return hasil

    def postorder(self):
        """Anak-anak -> Node."""
        hasil = []
        def kunjungi(node):
            for anak in node.bawahan:
                kunjungi(anak)
            hasil.append(node)
        kunjungi(self.root)
        return hasil


def bangun_struktur_baru():
    """Struktur organisasi sesuai gambar pada soal nomor 11."""
    t = TreeOrganisasi(Node("Rektor", "Root"))
    data = [
        ("Rektor", "Senat Universitas", "Senat"),
        ("Rektor", "Wakil Rektor I", "Bidang Akademik"),
        ("Rektor", "Wakil Rektor II", "Bidang Administrasi Umum & Keuangan"),
        ("Rektor", "Wakil Rektor III", "Bidang Kemahasiswaan & Kerja Sama"),
        ("Rektor", "Dekan Fakultas Sains dan Teknologi", "Dekan"),
        ("Dekan Fakultas Sains dan Teknologi", "Wakil Dekan I", "Bidang Akademik & Kelembagaan"),
        ("Dekan Fakultas Sains dan Teknologi", "Wakil Dekan II", "Bidang AUPK"),
        ("Dekan Fakultas Sains dan Teknologi", "Wakil Dekan III", "Bidang Kemahasiswaan"),
        ("Dekan Fakultas Sains dan Teknologi", "Ketua Program Studi Teknik Informatika", "Kaprodi"),
        ("Ketua Program Studi Teknik Informatika", "Sekretaris Program Studi", "Sekretaris"),
        ("Ketua Program Studi Teknik Informatika", "Kepala Laboratorium Komputer", "Kepala Lab"),
        ("Kepala Laboratorium Komputer", "Asisten Laboratorium", "Asisten"),
        ("Kepala Laboratorium Komputer", "Teknisi Laboratorium", "Teknisi"),
        ("Ketua Program Studi Teknik Informatika", "Koordinator Dosen", "Koordinator"),
        ("Koordinator Dosen", "Dosen Pembimbing Akademik", "Dosen"),
        ("Dosen Pembimbing Akademik", "Mahasiswa Bimbingan", "Leaf"),
        ("Koordinator Dosen", "Dosen Pengampu Mata Kuliah", "Dosen"),
    ]
    for d in data:
        t.insert_node(*d)
    return t


if __name__ == "__main__":
    t = bangun_struktur_baru()

    # Uji insert_node
    print("Insert atasan tidak ada:", t.insert_node("Tidak Ada", "X", "Dosen"))

    # Uji search_node
    for kata in ("dosen", "wakil", "kaprodi", "xyz"):
        print(f"\nCari '{kata}':")
        for n in t.search_node(kata):
            print("  -", n)

    # Uji traversal
    tampil = lambda daftar: " -> ".join(n.nama for n in daftar)
    print("\nPre-order :", tampil(t.preorder()))
    print("In-order  :", tampil(t.inorder()))
    print("Post-order:", tampil(t.postorder()))
