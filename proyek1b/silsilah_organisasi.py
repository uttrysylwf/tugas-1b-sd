"""Silsilah Organisasi UIN Suska Riau (prototype) - General Tree.
Nama pegawai adalah data fiktif. Jalankan: python silsilah_organisasi.py"""


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


def bangun_contoh():
    t = TreeOrganisasi(Node("Ahmad Fauzi", "Rektor"))
    data = [
        ("Ahmad Fauzi", "Budi Santoso", "Dekan FST"),
        ("Ahmad Fauzi", "Citra Lestari", "Dekan Syariah dan Hukum"),
        ("Budi Santoso", "Rina Marlina", "Ketua Prodi Teknik Informatika"),
        ("Budi Santoso", "Fajar Nugroho", "Ketua Prodi Sistem Informasi"),
        ("Citra Lestari", "Siti Aminah", "Ketua Prodi Hukum Keluarga"),
        ("Rina Marlina", "Andi Saputra", "Dosen Struktur Data"),
        ("Rina Marlina", "Maya Putri", "Dosen Basis Data"),
        ("Fajar Nugroho", "Lia Ramadhani", "Dosen Rekayasa Perangkat Lunak"),
        ("Siti Aminah", "Umar Faruq", "Dosen Hukum Perdata Islam"),
    ]
    for d in data:
        t.insert_node(*d)
    return t


if __name__ == "__main__":
    t = bangun_contoh()
    t.insert_node("Rina Marlina", "Wahyu Hidayat", "Staf Administrasi Prodi TI")
    t.insert_node("Fajar Nugroho", "Galih Permana", "Dosen Jaringan Komputer")
    print("Insert atasan tidak ada:", t.insert_node("Tidak Ada", "X", "Dosen"))
    for kata in ("dosen", "Rina", "ketua prodi", "xyz"):
        print(f"\nCari '{kata}':")
        for n in t.search_node(kata):
            print("  -", n)
    tampil = lambda daftar: " -> ".join(n.nama for n in daftar)
    print("\nPre-order :", tampil(t.preorder()))
    print("In-order  :", tampil(t.inorder()))
    print("Post-order:", tampil(t.postorder()))
