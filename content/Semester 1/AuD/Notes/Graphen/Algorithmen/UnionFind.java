static class UnionFind {

    private ArrayList<Integer>[] members;
    private int[] rep;

    public UnionFind(int n) {
        rep = new int[n];
        for (int i = 0; i < n; i++) {
            rep[i] = i;
        }

        members = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            members[i] = new ArrayList<Integer>();
            members[i].add(i);
        }
    }

    public boolean same(int u, int v) {
        return rep[u] == rep[v];
    }

    public void union(int u, int v) {
        boolean u_smaller_v = members[rep[u]].size() < members[rep[v]].size();
        int small = u_smaller_v ? u : v;
        int large = u_smaller_v ? v : u;

        ArrayList<Integer> small_list = members[rep[small]];
        for (int k : small_list) {
            rep[k] = rep[large];
            members[rep[large]].add(k);
        }
    }
}